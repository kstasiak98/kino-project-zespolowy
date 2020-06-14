<template>
 <v-card xs12 wrap style="text-align: center" class="pa-6">
   <h1>Wprowadź dane:</h1>
   <v-text-field
       v-model="imie"
       label="Podaj Imie"></v-text-field>
   <v-text-field
       v-model="nazwisko"
       label="Podaj Nazwisko"></v-text-field>
   <v-text-field
     v-model="login"
     label="Podaj login"></v-text-field>
   <v-text-field
     v-model="email"
     label="Podaj email"></v-text-field>
   <v-text-field
     v-model="password"
     :type="'password'"
     @click:append="showPassword = !showPassword"
     label="Podaj hasło"></v-text-field>
   <v-btn @click="postPost">ZAREJESTRUJ SIE</v-btn>
 </v-card>
</template>

<script>
import axios from 'axios';
import { CSRF_TOKEN } from "@/common/csrf_token"

export default {
  name: 'RegisterPage',
  data() {
    return {
        imie: '',
        nazwisko: '',
      login: '',
      email: '',
      password: '',
    };
  },
  methods: {
    postPost() {
      axios.post(
          '/api/client/',
          {
              "imie": this.imie,
              "nazwisko": this.nazwisko,
              "login": this.login,
              "email": this.email,
              "haslo": this.password
          },
          {
              headers: {"X-CSRFTOKEN": CSRF_TOKEN}
          },


      )
          .then(function(response) {
              console.log(response);
          })
          .catch(function(error) {
              console.log(error);
          });
        this.$router.push('/information');
    },
  },
};
</script>

<style scoped>

</style>
