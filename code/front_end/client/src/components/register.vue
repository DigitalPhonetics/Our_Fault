<template>
  <div class="formcontainer">
    <b-card bg-variant="light">
      <alert 
        :message="message"
        :alter_variant="alert_variant"
        v-if="showMessage"
      />
      <b-form @submit="sendRegisterInfo">
        <b-form-group
          id="input-group-1"
          label="Username"
          label-for="input-1"
          description="Please select an anonymus username for maximum privacy."
        >
          <b-form-input
            id="input-1"
            v-model="form.userid"
            type="userid"
            required
            placeholder="Enter userid"
          />
          <b-form-invalid-feedback :state="validUserid">
            Please enter a valid userid (between 3 and 15 Charcters long).
          </b-form-invalid-feedback>
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
          <b-form-invalid-feedback 
            :state="validPassword"
          >
            Your password must have a length between 3 and 15 Characters.
          </b-form-invalid-feedback>
        </b-form-group>

         <b-form-group 
          id="input-group-3"
          label="Repeat Password:"
          label-for="input-3"
        >
          <b-form-input
            id="input-3"
            v-model="form.pwd_repeat"
            required
            type="password"
          />
          <b-form-invalid-feedback 
            :state="confirmedPassword"
          >
            Your passwords must match.
          </b-form-invalid-feedback>
        </b-form-group>

        <b-form-group>
          <b-form-checkbox
            id="checkbox-consent"
            v-model="form.consent"
            value="true"
            unchecked-value="false"
            name="checkbox-consent"
          >
            I accept the terms of use: <br>
            <p>
              I agree to transmit my username and password in human readable text for registration and login on this website.
              Furthermore, I grant the rights to store the username as human readable text and the password in encrypted form for the duration of this user study.
              Additionally, I allow transmitting and storing of all text-based conversations (annotated with my username) with the dialog system on this website in human-readable form 
              as well as their anonymized usage in a related research study.
            </p>
          </b-form-checkbox>
          <b-form-invalid-feedback 
            :state="userConsent"
          >
            You must agree to the service usage terms to be able to continue.
          </b-form-invalid-feedback>
        </b-form-group>

        <b-button 
          variant="primary"
          type="submit"
          :disabled="!checkRegisterInfo()"
        >
          Register
        </b-button> 
      </b-form>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  name: 'Register',
  data() {
    return {
      message: null,
      showMessage: false,
      alert_variant: 'danger',
      form: {
          userid: '',
          pwd: '',
          pwd_repeat: '',
          consent: 'false',
      },
    }
  },
  components: {
    alert: Alert,
  },
  computed: {
    validPassword() {
        return this.form.pwd.length >= 3 && this.form.pwd.length <= 15;
    },
    confirmedPassword() {
        return this.form.pwd === this.form.pwd_repeat;
    },
    validUserid() {
      // const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      // return re.test(this.form.email);
        return this.form.userid.length >= 3 && this.form.userid.length <=15;
    },
    userConsent() {
      return this.form.consent === 'true';
    }
  },
  methods: {
    checkRegisterInfo: function() {
       // validate inputs
      if (this.validUserid === false || this.validPassword === false || this.confirmedPassword === false || this.userConsent === false) {
          return false;
      } else {
        return true;
      }
    },
    sendRegisterInfo: function (event) {
        event.preventDefault();

        if(this.checkRegisterInfo() === true) {
          const path = 'http://127.0.0.1:44123/register';
          axios.post(path, 
              { 
                  userid: this.form.userid, 
                  pwd: this.form.pwd,
              }
          )
          .then((response) => {
              this.message = "Registered successfully :)";
              this.alert_variant = response.data.status === 'success' ? 'success' : 'danger';
              this.showMessage = true;
              this.$router.push({
                name: 'Login',
                params: {
                  registered_successfull: true,
                },
              });
          })
          .catch((error) => {
              if (error.response.status === 401) {
                this.message = 'User already exists';
              } else {
                this.message = error;
              }
              this.alert_variant = 'danger';
              this.showMessage = true;
          });
        }
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
