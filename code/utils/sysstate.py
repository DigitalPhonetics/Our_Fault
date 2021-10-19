from utils.transmittable import Transmittable
from utils.sysact import SysAct

class SysState(Transmittable):

    def __init__(self, last_acts: SysAct = None, last_offer: str = None, last_request_slot: str = None, lastInformedPrimKeyVal: str = None):
        self.last_acts = last_acts
        self.last_offer = last_offer
        self.last_request_slot = last_request_slot
        self.lastInformedPrimKeyVal = lastInformedPrimKeyVal

    def serialize(self):
        return {
            'last_acts': [act.serialize() if act else act for act in self.last_acts],
            'last_offer': self.last_offer,
            'last_request_slot': self.last_request_slot,
            'lastInformedPrimKeyVal': self.lastInformedPrimKeyVal
        }

    @staticmethod
    def deserialize(obj: dict):
        serialized_last_acts = obj['last_acts']
        last_acts = [SysAct.deserialize(act) if act else act for act in serialized_last_acts]
        return SysState(last_acts=last_acts, last_offer=obj['last_offer'], last_request_slot=obj['last_request_slot'], lastInformedPrimKeyVal=obj['lastInformedPrimKeyVal'])