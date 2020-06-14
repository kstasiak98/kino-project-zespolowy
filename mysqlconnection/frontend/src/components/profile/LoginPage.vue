<template>
  <v-container>
    <v-row  style="text-align: center">
      {{UserArray}}
      <v-col>
        <v-card style="text-align: center" class="pa-6">
          <h1>Podaj dane:</h1>
          <v-spacer></v-spacer>
          <v-text-field
            v-model="logins"
            label="Podaj login"></v-text-field>
          <v-text-field
            v-model="password"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPassword ? 'text' : 'password'"
            @click:append="showPassword = !showPassword"
            label="Podaj hasło"></v-text-field>
          <v-btn @click="checkUser">ZALOGUJ</v-btn>
        </v-card>
      </v-col>
      <v-col xs12 wrap>
        <v-card  style="text-align: center" class="pa-6">
          <h2>Nie masz konta?</h2>
          <v-spacer></v-spacer>
          <br/>
          <v-btn @click="onClick = !onClick">Zarejestruj sie</v-btn>
        </v-card>
        <template v-if="onClick===true">
          <br />
          <register-page></register-page>
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';
import RegisterPage from './RegisterPage.vue';
import {CSRF_TOKEN} from "@/common/csrf_token";
// import { UserBase } from '../DATA/userdata';


// function jasonParsait() {
  // const nowyJasonTABLE = [
  //   { CarID: 123 },
  //   { CarID: 456 },
  //   { CarID: 789 },
  // ];
  // const nowyJasonTABLEstring = `[
  //   { "CarID" : 123 },
  //   { "CarID" : 456 },
  //   { "CarID" : 789 }
  // ]`;
  // Zmiana na ciąg który przesyłamy przez przeglądarkę
  // const carIDstringify = JSON.stringify(nowyJasonTABLE);
  // console.log(carIDstringify);
  // console.log(typeof (carIDstringify));
  // Zmiana na normalny java script
  // const carIDjson = JSON.parse(nowyJasonTABLEstring);
  // console.log(carIDjson);
  // console.log(typeof (carIDjson));
// }

export default {
  name: 'LoginPage',
  components: { RegisterPage },

  data() {
    return {
      userOnline: {},
      logins: '',
      password: '',
      showPassword: false,
      onClick: false,
      USERB: null,
      UserArray: [],

    };
  },
    mounted() {
        this.checkLogin();
      this.getUsersBase();

    },
  methods: {
      checkLogin(){
          if (this.$store.state.ifLogin === true)
              this.$router.push('/login/profile');

      },
    getUsersBase() {
        axios.get('/api/client/',
          {
              headers: {"X-CSRFTOKEN": CSRF_TOKEN}
          }
      ).then(response => {
            this.UserArray = response.data;
        })
    },
    logging() {
      this.$router.push('/login/profile');
    },
      checkUser() {

        for( let i = 0; i < this.UserArray.length; i += 1){
            if (this.logins === this.UserArray[i].login) {
                if (this.password === this.UserArray[i].haslo) {
                    const user = {
                        login: this.UserArray[i].login,
                        id: this.UserArray[i].klient_id,
                        email: this.UserArray[i].email,
                        punkty: 0,
                    };
                    this.$store.commit('setUser', user);
                    this.logging();
                }
            }

        }
      }
  },
};
</script>

<style scoped>

</style>
