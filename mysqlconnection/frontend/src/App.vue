<template>
  <v-app>
    <v-app-bar app color="blue">
      <div class="d-flex align-center">
        <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        />
      </div>

      <v-spacer></v-spacer>
      <v-divider vertical class="mx-2"></v-divider>
      <router-link class="nav-link" :to="{ name: 'Home' }">HOME</router-link>
      <v-divider vertical class="mx-2"></v-divider>
      <router-link class="nav-link" :to="{ name: 'Repertoire' }"
        >REPERTUAR</router-link
      >
      <v-divider vertical class="mx-2"></v-divider>
      <router-link class="nav-link" :to="{ name: 'Store' }"
        >WYBÓR BILETU</router-link
      >
      <v-divider vertical class="mx-2"></v-divider>
      <router-link class="nav-link" :to="{ name: 'Ticket' }"
        >BILETY</router-link
      >
    </v-app-bar>

    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  })
};
</script>

<style>
.nav-link {
  text-decoration: none;
  color: inherit;
}
</style>
