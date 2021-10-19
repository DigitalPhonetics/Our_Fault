<template>
  <fragment>
    <!-- <div v-if="has_token && !this.started">
      <b-button
        variant="warning"
        @click="startDialog"
      >
        Start Dialog
      </b-button>
    </div> -->
    <div v-if="has_token" class="messagebox" ref="messagebox">
      <chatmessage
        v-for="(msg, index) in messages"
          :key="index"
          :party="msg.party"
          :message="msg.message"
      />
    </div>
    <div v-if="has_token" class="footer">
        <input 
          ref="sysmsg"
          id="sysmsg"
          placeholder="Enter your message here"
          v-model="sysMessage"
          @keyup.enter="sendMessage"
          style="flex:1; display:block;"/>
        <b-button
          variant="primary"
          :disabled="!connected"
          @click="sendMessage"
        >
          Send
        </b-button>
    </div>
    <b-modal id="connectionalert" hide-footer>
      <template v-slot:modal-title>
        No valid connection to server
      </template>
      <div>
         Login expired (or connection problem) - please try to log in again!
      </div>
      <b-button @click="$router.replace('/')" block variant="danger">Login</b-button>
    </b-modal>
  </fragment>
</template>

<script>
import axios from 'axios';
import Chatmessage from './chatmessage.vue';
import { mapState } from "vuex";

export default {
    name: 'Chat',
    components: {
      chatmessage: Chatmessage,
    },
    computed: {
      
      ...mapState(["token"]),
    },
    created() {
      if(this.has_token()) {
        // only setup a connection if we get a token from server
        this.socket = new WebSocket("ws://127.0.0.1:44123/woz?token=" + this.token);
        this.socket.onopen = (event) => {
          this.startDialog();
        };
        this.socket.onmessage = (msg) => {
          this.messages.push({party: 'user', message: msg.data});
        }
      }
      else {
        // don't connect - no token
      }
    },
    updated() {
      this.$nextTick(() => this.scrollToBottom()); // scroll to bottom of chat messages
      this.$refs.sysmsg.focus();                  // focus chat message input
    },
    data() {
      return {
          socket: null,
          messages: [],
          sysMessage: '',
          connected: false,
          domain: null,
          started: false
      } 
    },
    methods: {
        has_token: function() {
            return (typeof this.token !== 'undefined') && (this.token != null) && (this.token.length > 0);
        },
        startDialog: function (domain_number) {
            if (this.has_token()) {
              this.started = true;
              this.messages = [];
              this.socket.send(JSON.stringify({
                  topic: "start_dialog",
                  domain: this.domain,
                  access_token: this.token,
                }
              ));
            } else {
              this.$bvModal.show('connectionalert'); 
            }
        },       
        sendMessage: function (event) {
          event.preventDefault();

          if (this.has_token()) {
            this.messages.push({party: 'system', message: this.sysMessage});
            this.socket.send(JSON.stringify({
              access_token: this.token,
              topic: 'sys_utterance',
              domain: this.domain,
              msg: this.sysMessage,
            }));
            this.sysMessage = '';
          } else {
            this.$bvModal.show('connectionalert');
          } 
        },
        scrollToBottom: function () {
          var container = this.$refs.messagebox;
          container.scrollTop = container.scrollHeight;
        },
    }
};
</script>

<style>
.footer
{
    position: absolute;
    bottom:30px;
    left:0px;
    right:0px;
    height:50px;
    margin-bottom:0px;
    display: flex;
}

.messagebox
{
    padding: 35px;
    height: calc(100vh - 100px);
    overflow-y: auto;
}

</style>
