<template>
  <v-row justify="center">
    <v-col>
      <v-card>
        <!--       <v-card-actions>-->
        <!--         <v-img-->
        <!--           :src="require('./image/incognito.jpg')"-->
        <!--         ></v-img>-->
        <!--       </v-card-actions>-->
        <v-card-text>
          <h1>WITAMY W PROFILU:</h1>
          <tr>
            <td><h3>Nazwa użytkownika:</h3></td>
            <td>{{ USSER.login }}</td>
          </tr>
          <tr>
            <td><h3>Poczta:</h3></td>
            <td>{{ USSER.email }}</td>
          </tr>
          <tr>
            <td><h3>Ilość punktów:</h3></td>
            <td>{{ USSER.punkty }}</td>
          </tr>
          <tr>
            <td><v-btn @click="goToTicket()">KUP BILETY</v-btn></td>
          </tr>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  name: "ProfilePage",
  data() {
    return {
      User: {
        login: "user1",
        email: "user1@wp.pl",
        punkty: "0"
      }
    };
  },
  methods: {
    goToTicket() {
      this.$router.push("/store");
    }
  },
  computed: {
    USSER() {
      return this.$store.state.userOnline;
    }
  },
  mounted() {
    console.log("USER", this.USSER);
  }
};
</script>

<style scoped></style>
