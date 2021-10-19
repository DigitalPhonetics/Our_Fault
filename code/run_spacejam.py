import datetime
from datetime import timedelta, datetime
from passlib.context import CryptContext
import jwt
import tornado.ioloop
import tornado.web
from tornado.websocket import WebSocketHandler
import json
import pymysql
import os

from services.space_jam.space_jam import Game, GameState
from services.service import PublishSubscribe, Service, DialogSystem
from services.nlu.space_jam_nlu import SpaceJamNLU
from services.bst.space_jam_bst import SpaceJamBST
from services.policy.space_jam_hdc_policy import SpaceJamHandcraftedPolicy
from services.nlg.space_jam_nlg import SpaceJamHandcraftedNLG
from services.hci import ConsoleInput, ConsoleOutput
from services.domain_tracker.domain_tracker import DomainTracker
from utils.topics import Topic
from utils.logger import DiasysLogger, LogLevel
from utils.domain.spacejamdomain import SpaceJamDomain
import time
from utils.sysact import SysActionType
from utils.useract import UserActionType

# to get a string like this run: openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 120
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = DiasysLogger(name="userlog", console_log_lvl=LogLevel.NONE, file_log_lvl=LogLevel.DIALOGS)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)


# create db
def create_userdb():
    try:
        if not os.path.isfile("users.mysqldb"):
            connection = pymysql.connect("localhost", "dbowner2", "abcd1234", "USERDB")
            print("DB Users not found - creating ")
            cursor = connection.cursor()
            # Tabelle erzeugen
            sql = """CREATE TABLE IF NOT EXISTS Users(
                userid VARCHAR(255) PRIMARY KEY,
                hash TEXT NOT NULL,
                disabled BOOL NOT NULL
                ); """
            cursor.execute(sql)
            connection.commit()
            cursor.close()
        else:
            print("DB Users was found - connection established")
            connection = pymysql.connect("localhost", "dbowner", "1!:xaw0?asd24", "USERDB")

        return connection
    except:
        import traceback
        print(traceback.format_exc())
        print("SQLERROR: Could not connect to database / create table failed")

dbconn = create_userdb()

def insert_user(dbconn, userid: str, pwd_plaintext: str):
    try:
        cursor = dbconn.cursor()
        cursor.execute(f"INSERT INTO Users(userid, hash, disabled) VALUES(%s,%s,FALSE)", (userid, get_password_hash(pwd_plaintext)))
        dbconn.commit()
        return True
    except:
        print("SQLERROR: Failed to create user:", userid)
        import traceback
        import sys
        traceback.print_exc(file=sys.stdout)
    return False

# try:
#     print("Creating testuser")
#     insert_user(dbconn, "abcd", "abcd")
# except:
#     print("Testuser exists already")

class User():
    def __init__(self, userid, hashed_password, disabled):
        super().__init__()
        self.userid = userid
        self.hashed_password = hashed_password
        self.disabled = disabled


def get_user(conn, userid: str):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE userid=%s", (userid,))
        result = cursor.fetchone()
        if result:
            return User(userid=userid, hashed_password=result[1], disabled=result[2])
    except:
        pass
    finally:
        cursor.close()
    return None

def authenticate_user(conn, userid: str, password: str):
    user = get_user(conn, userid)
    if not user:
        print(f"ACCESS WARNING: user '{userid}' not in DB")
        return False
    if not verify_password(password, user.hashed_password):
        print(f"ACCESS WARNING: wrong password for user '{userid}'")
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt.decode("utf-8")

def user_from_token(token):
    """ Extract userid from token, if token is still valid.
    If user is registered + token is not expired, returns userid
    else, return None
    """
    try:
        # automatically checks expired property
        jwt_payload = jwt.decode(token, SECRET_KEY, verify=True, algorithm=ALGORITHM)
        if 'userid' in jwt_payload:
            return jwt_payload['userid']
    except:
        pass
    return None


class CorsJsonHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # allow requests from anywhere (CORS)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,access-control-allow-origin,authorization,content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()
    
    def prepare(self):
        # extract json
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None


class LoginHandler(CorsJsonHandler):
    def post(self):
        if self.json_args:
            userid = self.json_args['userid']
            pwd_plaintext = self.json_args['pwd']
            user = authenticate_user(dbconn, userid, pwd_plaintext)
            if user:
                logger.dialog_turn(f"USER {userid} LOGGED IN")
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = create_access_token(data={"userid": userid}, expires_delta=access_token_expires)
                self.write({"access_token": access_token})
                self.set_status(200)
            else:
                logger.dialog_turn("FAILED LOGIN ATTEMPT")
                self.set_status(401, reason="Unauthorized")
        else:
            self.set_status(402, reason="Expected JSON")
        self.finish()

class RegisterHandler(CorsJsonHandler):
    def post(self):
        if self.json_args:
            userid = self.json_args['userid']
            pwd_plaintext = self.json_args['pwd']

            print("registering user", userid)
            if get_user(dbconn, userid):
                print(f"user {userid} already exists")
                self.set_status(401, reason="User already exists")
            else:
                if not insert_user(dbconn, userid=userid, pwd_plaintext=pwd_plaintext):
                    self.set_status(402, reason="Error while creating new User")
        else:
            self.set_status(403, reason="Expected JSON")
        self.finish() 


import asyncio
class GUIServer(Service):
    def __init__(self, domains, logger, game_rules, game_state):
        super().__init__(domain="", debug_logger=logger)
        self.websockets = {}
        # self.woz_web_sockets = {}
        self.domains = domains
        self.logger = logger
        self.game_rules = game_rules
        self.game_state = game_state
        self.loopy_loop = asyncio.new_event_loop()

    def dialog_start(self, user_id: str):
        self.game_state.reset()
        self.forward_message_to_react(message=self.game_state.slider, topic='slider', user_id=user_id)
        for i in range(len(self.game_state.dials)):
            self.forward_message_to_react(message=self.game_state.dials[i].start_position, topic=f"dial_{i}", user_id=user_id)
        button_pos = self.game_state.memory_stages[0]
        # TODO: remove after WOZ study!
        asyncio.set_event_loop(asyncio.new_event_loop())
        # self.woz_web_sockets[user_id].write_message("Dialog Started")

        self.forward_message_to_react(message=f"memory_{button_pos['sys_button'][0]}_{button_pos['sys_button'][1]}", topic="memory", user_id=user_id)
        self.forward_message_to_react(message="", topic="button_sequence", user_id=user_id)
        self.forward_message_to_react(message="", topic="toggles", user_id=user_id)
        self.set_state(user_id, "current_module", 0)
        self.set_state(user_id, "last_user_acts", [])

    @PublishSubscribe(sub_topics=["user_acts", "sys_state"])
    def pay_attention_to_reset(self, user_id, sys_state, user_acts):
        current_module = self.get_state(user_id, "current_module")
        last_user_acts = self.get_state(user_id, 'last_user_acts')
        self.set_state(user_id, "last_user_acts", user_acts)

        if SysActionType.NextModule in [act.type for act in sys_state.last_acts]:
            current_module += 1
            self.set_state(user_id, "current_module", current_module)
        if UserActionType.Confirm in [act.type for act in user_acts] and UserActionType.Restart in [act.type for act in last_user_acts]:
            if current_module == 1:
                self.game_state.reset_dials()
                for i in range(len(self.game_state.dials)):
                    self.forward_message_to_react(message=self.game_state.dials[i].start_position, topic=f"dial_{i}", user_id=user_id)
                self.forward_message_to_react(message="dial_complete", topic="module_incomplete", user_id=user_id)
            elif current_module == 2:
                self.game_state.reset_button_sequence()
                self.forward_message_to_react(message="button_sequence_complete", topic="module_incomplete", user_id=user_id)
                self.forward_message_to_react(message="", topic="button_sequence", user_id=user_id)
            elif current_module == 3:
                self.game_state.reset_toggle_switches()
                self.forward_message_to_react(message="", topic="toggles", user_id=user_id)
                self.forward_message_to_react(message="toggle_complete", topic="module_incomplete", user_id=user_id)
            elif current_module == 4:
                self.game_state.reset_memory()
                button_pos = self.game_state.memory_stages[0]
                self.forward_message_to_react(message=f"memory_{button_pos['sys_button'][0]}_{button_pos['sys_button'][1]}", topic="memory", user_id=user_id)
                self.forward_message_to_react(message="memory_complete", topic="module_incomplete", user_id=user_id)                                                       



    def button_event(self, user_id, button_id, button_active):
        if "sequence" in button_id:
            self.button_sequence_event(user_id=user_id, button_id=button_id)
        elif "memory" in button_id:
            self.memory_event(user_id=user_id, button_id=button_id, button_active=button_active)

    def button_sequence_event(self, user_id, button_id):
        self.game_state.update_button_sequence(button_id)
        success = self.game_rules.is_button_sequence_module_complete(self.game_state)
        if success:
            self.game_state.add_complete_modules()
            self.forward_message_to_react(message="button_sequence_complete", topic="module_complete", user_id=user_id)
            self.forward_message_to_react(message=self.game_state.new_slider_pos(), topic="slider", user_id=user_id)
        else:
            self.forward_message_to_react(message="15", topic="time_penalty", user_id=user_id)
            time.sleep(0.3)
            self.game_state.reset_button_sequence()
            self.forward_message_to_react(message="button_sequence_complete", topic="module_incomplete", user_id=user_id)
            self.forward_message_to_react(message="", topic="button_sequence", user_id=user_id)

    def memory_event(self, user_id, button_id, button_active):
        self.game_state.update_memory(button_id, button_active)
        success = self.game_rules.is_memory_module_complete(self.game_state)
        if success == True:
            self.game_state.add_complete_modules()
            self.forward_message_to_react(message="memory_complete", topic="module_complete", user_id=user_id)
            self.forward_message_to_react(message=self.game_state.new_slider_pos(), topic="slider", user_id=user_id)
        elif success == False:
            self.forward_message_to_react(message="15", topic="time_penalty", user_id=user_id)            
            time.sleep(0.3)
            self.game_state.reset_memory()
            button_pos = self.game_state.memory_stages[0]
            self.forward_message_to_react(message=f"memory_{button_pos['sys_button'][0]}_{button_pos['sys_button'][1]}", topic="memory", user_id=user_id)
            self.forward_message_to_react(message="memory_complete", topic="module_incomplete", user_id=user_id)
        else:
            time.sleep(0.3)
            self.game_state.next_memory_stage()
            button_pos = self.game_state.memory_stages[self.game_state.memory_stage]
            self.forward_message_to_react(message=f"memory_{button_pos['sys_button'][0]}_{button_pos['sys_button'][1]}", topic="memory", user_id=user_id)



    def dial_event(self, user_id, dial_id, dial_position):
        self.game_state.update_dials(dial_id, dial_position)
        success = self.game_rules.is_dial_module_complete(self.game_state)
        if success == True:
            self.game_state.add_complete_modules()
            self.forward_message_to_react(message="dial_complete", topic="module_complete", user_id=user_id)
            self.forward_message_to_react(message=self.game_state.new_slider_pos(), topic="slider", user_id=user_id)
        elif success == False:
            self.forward_message_to_react(message="15", topic="time_penalty", user_id=user_id)                
            time.sleep(0.3)
            self.game_state.reset_dials()
            for i in range(len(self.game_state.dials)):
                self.forward_message_to_react(message=self.game_state.dials[i].start_position, topic=f"dial_{i}", user_id=user_id)
            self.forward_message_to_react(message="dial_complete", topic="module_incomplete", user_id=user_id)

    def toggle_switch_event(self, user_id, toggle_id, toggle_active):
        self.game_state.update_toggle_switches(toggle_id, toggle_active)
        success = self.game_rules.is_toggle_switch_module_complete(self.game_state)
        if success == True:
            self.game_state.add_complete_modules()
            self.forward_message_to_react(message="toggle_complete", topic="module_complete", user_id=user_id)
            self.forward_message_to_react(message=self.game_state.new_slider_pos(), topic="slider", user_id=user_id)
        elif success == False:
            self.forward_message_to_react(message="15", topic="time_penalty", user_id=user_id)            
            time.sleep(0.3)
            self.game_state.reset_toggle_switches()
            self.forward_message_to_react(message="", topic="toggles", user_id=user_id)
            self.forward_message_to_react(message="toggle_complete", topic="module_incomplete", user_id=user_id)

    # @PublishSubscribe(pub_topics=["sys_utterance"])
    # def woz_system_response(self, user_id: str = "default", sys_utterance = ""):
    #     self.logger.dialog_turn(f"# USER {user_id} # USR-UTTERANCE ({sys_utterance}")
    #     return {'sys_utterance': sys_utterance, 'user_id': user_id}

    @PublishSubscribe(pub_topics=["sys_utterance"])
    def game_over(self, user_id: str = "default", condition="defeat"):
        # self.woz_web_sockets[user_id].write_message(f"Game over; {condition}")
        self.logger.dialog_turn(f"USER {user_id} GAME OVER; CONDITION: {condition.upper()}")
        return {f"sys_utterance/{self.domains[0].get_domain_name()}": f"Thank you for playing! Don't forget your id for the questionairre is: {user_id}",
                "user_id": user_id}

    def log_consent(self, user_id: str = "default"):
        self.logger.dialog_turn(f"# USER {user_id} CONSENTED TO DATA AGREEMENT")

    @PublishSubscribe(pub_topics=['user_utterance'])
    def user_utterance(self, user_id = "default", domain_idx = 0, message = ""):
        try:
            self.logger.dialog_turn(f"# USER {user_id} # USR-UTTERANCE ({self.domains[domain_idx].get_domain_name()}) - {message}")

            # forward message to woz
            asyncio.set_event_loop(self.loopy_loop)
            # self.woz_web_sockets[user_id].write_message(message)

            return {f'user_utterance/{self.domains[domain_idx].get_domain_name()}': message, "user_id": user_id}
        except:
            print("ERROR in GUIService - user_utterance: user=", user_id, "domain_idx=", domain_idx, "message=", message)
            import traceback
            import sys
            traceback.print_exc(file=sys.stdout)
            return {}        

    def light_button(self, user_id, button_id):
        self.forward_message_to_react(message=button_id, topic="memory", user_id=user_id)

    @PublishSubscribe(sub_topics=['sys_utterance'])
    def forward_sys_utterance(self, user_id: str, sys_utterance: str):
        self.forward_message_to_react(message=sys_utterance, topic="sys_utterance", user_id=user_id,) 

    def forward_message_to_react(self, message, topic: str, user_id: str = "default"):
        asyncio.set_event_loop(self.loopy_loop)
        self.websockets[user_id].write_message({"topic": topic, "msg": message})


d = SpaceJamDomain("SpaceJam")
nlu = SpaceJamNLU(domain=d, logger=logger)
bst = SpaceJamBST(domain=d,logger=logger)
policy = SpaceJamHandcraftedPolicy(domain=d, logger=logger)
nlg = SpaceJamHandcraftedNLG(domain=d, logger=logger)
user_in = ConsoleInput()
user_out = ConsoleOutput()
# tracker = DomainTracker([d])
domains = [d]
game = Game(d, logger=logger)
game_state = GameState()
gui_service = GUIServer(domains, logger, game_rules=game, game_state=game_state)
services = [nlu, bst, policy, nlg, gui_service]
ds = DialogSystem(services=services, debug_logger=logger)
error_free = ds.is_error_free_messaging_pipeline()
if not error_free:
    ds.print_inconsistencies()
# ds.draw_system_graph()
# ds.run_dialog({'gen_user_utterance': ""})


class SimpleWebSocket(tornado.websocket.WebSocketHandler):

    def _extract_token(self, uri):
        start=len("/ws?token=")
        return uri[start:]

    def open(self, *args):
        token = self._extract_token(self.request.uri)
        userid = user_from_token(token)
        if userid:
            gui_service.websockets[userid] = self
 
    def on_message(self, message):
        data = json.loads(message)
        # check token validity
        user_id = user_from_token(data['access_token'])
        if user_id:
            topic = data['topic']
            domain_index = 0
            if topic == 'start_dialog':
                logger.dialog_turn(f"# USER {user_id} # DIALOG-START ({domains[domain_index].get_domain_name()})")
                ds._start_dialog(start_signals={f'user_utterance/{domains[domain_index].get_domain_name()}': ''}, user_id=user_id)
                logger.dialog_turn(f"SUCCESSFULLY STARTED DIALOG for USER{user_id}")
            elif topic == 'user_utterance':
                gui_service.user_utterance(user_id=user_id, domain_idx=domain_index, message=data['msg'])
            elif topic == 'button_event':
                gui_service.button_event(user_id=user_id, button_id=data['id'], button_active=data['active'])
            elif topic == 'dial_event':
                gui_service.dial_event(user_id=user_id, dial_id=data['id'], dial_position=data['position'])
            elif topic == "toggle_switch_event":
                gui_service.toggle_switch_event(user_id=user_id, toggle_id=data['id'], toggle_active=data['active'])
            elif topic == "game_over":
                gui_service.game_over(user_id=user_id, condition=str(data['condition']))
            elif topic == "user_consented":
                gui_service.log_consent(user_id=user_id)
    
    def on_close(self):
        # find right connection to delete
        for userid in gui_service.websockets:
            if gui_service.websockets[userid] == self:
                logger.dialog_turn(f"# USER {userid} # SOCKET-CLOSE")
                del gui_service.websockets[userid]
                break

    def check_origin(self, *args, **kwargs):
        # allow cross-origin
        return True

# class WOZWebSocket(tornado.websocket.WebSocketHandler):

#     def _extract_token(self, uri):
#         start=len("/woz?token=")
#         return uri[start:]

#     def open(self, *args):
#         token = self._extract_token(self.request.uri)
#         userid = user_from_token(token)
#         if userid:
#             gui_service.woz_web_sockets[userid] = self
 
#     def on_message(self, message):
#         data = json.loads(message)
#         # check token validity
#         user_id = user_from_token(data['access_token'])
#         if user_id:
#             topic = data['topic']
#             domain_index = 0
#             if topic == "sys_utterance":
#                 gui_service.woz_system_response(user_id=user_id, sys_utterance=data['msg'])
    
#     def on_close(self):
#         # find right connection to delete
#         for userid in gui_service.websockets:
#             if gui_service.websockets[userid] == self:
#                 logger.dialog_turn(f"# USER {userid} # SOCKET-CLOSE")
#                 del gui_service.websockets[userid]
#                 break

#     def check_origin(self, *args, **kwargs):
#         # allow cross-origin
#         return True


def make_app():
    return tornado.web.Application([
        (r"/login", LoginHandler),
        (r"/register", RegisterHandler),
        (r"/ws", SimpleWebSocket)  # ,
        # (r"/woz", WOZWebSocket)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(44123)
    tornado.ioloop.IOLoop.current().start()