<template>
  <div class="formcontainer">
    <b-card bg-variant="light">
      <alert 
        :alter_variant="success"
        v-if="registered_successfull"
        :message="registered_successfull_msg"
      />
      <alert 
        :message="message"
        :alter_variant="alert_variant"
        v-if="showMessage"
      />
      <b-form @submit="sendLoginInfo">
        <b-form-group
          id="input-group-1"
          label="Username:"
          label-for="input-1"
        >
          <b-form-input
            id="input-1"
            v-model="form.userid"
            type="text"
            required
            placeholder="Your username"
          />
        </b-form-group>

        <b-form-group 
          id="input-group-2"
          label="Password:"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.pwd"
            required
            type="password"
          />
        </b-form-group>

        <b-button 
          variant="primary"
          type="submit"
        >
          Login
        </b-button> 
        <p>
          No Account yet? <router-link to="/register">Register here</router-link>
        </p>
      </b-form>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Login',
  props: {
    registered_successfull: false,
  },
  data() {
    return {
      message: null,
      showMessage: false,
      alert_variant: 'danger',
      form: {
          userid: '',
          pwd: '',
      },
      registered_successfull_msg: 'Registered successfully! Please log in here.',
    }
  },
  components: {
    alert: Alert,
  },
  methods: {
    sendLoginInfo: function (event) {
        event.preventDefault();
        this.registered_successfull = false; // hide registration alert

        const path = 'http://127.0.0.1:44123/login';
        axios.post(path, 
            { 
                userid: this.form.userid, 
                pwd: this.form.pwd,  
            }
        )
        .then((response) => {
            this.message = "Logged in :)";
            this.alert_variant = response.data.status === 'success' ? 'success' : 'danger';
            this.showMessage = true;
            this.$store.dispatch("login", { token: response.data.access_token });
            this.$router.push({
              name: 'Tutorial',
            });
        })
        .catch((error) => {
            console.log("ERRR");
            console.log(error.response.status);
            // eslint-disable-next-line
            if (error.response.status === 401) {
                this.message = 'Login error: wrong username or password';
            } else {
                this.message = error;
            }
            this.alert_variant = 'danger';
            this.showMessage = true;
        });
    },
  },
  created() {
  },
};
</script>

<style scoped>

h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.formcontainer {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>
