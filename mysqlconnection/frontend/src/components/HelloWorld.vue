<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <!--      <v-col class="mb-4">-->
      <!--        <h1 class="display-2 font-weight-bold mb-3">-->
      <!--          Welcome to Vuetify-->
      <!--        </h1>-->

      <!--        <p class="subheading font-weight-regular">-->
      <!--          For help and collaboration with other Vuetify developers,-->
      <!--          <br />please join our online-->
      <!--          <a href="https://community.vuetifyjs.com" target="_blank"-->
      <!--            >Discord Community</a-->
      <!--          >-->
      <!--        </p>-->
      <!--      </v-col>-->
      <v-col cols="12">
        <v-card>
          <h1>Witamy na stronie kina</h1>
          <div>Co chciałbyś zrobić?</div>
          <v-spacer></v-spacer>
          <v-flex mt-4 xs12>
            <v-btn to="/login">ZALOGUJ SIE</v-btn>
            <v-btn to="/repertoire">REPERTUAR</v-btn>
          </v-flex>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({}),
  computed: {
    UserOnlineIF() {
      return this.$store.state.userOnline;
    },
    userLogged() {
      return this.$store.state.ifLogin;
    }
  }
};
</script>
