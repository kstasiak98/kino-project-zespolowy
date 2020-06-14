<template>
  <v-row align-content="center" justify="center">
    <v-col cols="4">
      <v-select
        label="wybierz interesujacy cie film..."
        v-model="value2"
        :items="Films"
        item-value="film_id"
        item-text="tytul"
      ></v-select>
    </v-col>
    <v-col cols="12" align-content="center" class="text-center">
      <v-card height="100px">
        <h2>Godziny i Daty seansów:</h2>
        <template v-for="(seans, index) in seans_table2">
          <template v-if="seans.film === value2">
            <v-btn :key="index" @click="pick_seans(seans)">
              {{ seans.data }} <br />
              {{ seans.godzina }}
            </v-btn>
            {{ seans.id }}
          </template>
        </template>
      </v-card>
    </v-col>
    <template v-if="pickedSeansID">
      <v-col cols="12">
        <SallPage
          :Sala="sall"
          :Seans="picked_seans"
          :seans-i-dnew="pickedSeansID"
        ></SallPage>
      </v-col>
    </template>
  </v-row>
</template>

<script>
import SallPage from "./SallPage.vue";
import { FILMS, SEANS } from "@/components/DATA/database";
import { apiService } from "@/common/api.service";

export default {
  name: "ShopPage",
  components: { SallPage },
  data: () => ({
    films_table: FILMS,
    seans_table: SEANS,
    value: null,
    tickets: [],
    seans_table2: [],
    value2: null,
    Films: [],
    pickedSeansID: null,
    sall: {
      id: 0,
      rows: 0,
      columns: 0
    },
    picked_seans: null,
    reserved: []
  }),
  created() {
    this.getFilms();
    this.getSeanse();
    this.getTickets();
  },
  computed: {
    items() {
      return this.films_table.map(film => {
        return film.title;
      });
    }
  },
  methods: {
    pick_sall(picked_sall, seans) {
      this.sall = picked_sall;
      this.picked_seans = seans;
    },
    getTickets() {
      let endpoint = `api/ticket/`;
      apiService(endpoint).then(data => {
        this.tickets = data;
      });
    },
    getFilms() {
      let endpoint = "api/films/";
      apiService(endpoint).then(data => {
        this.Films.push(...data);
      });
    },
    getSeanse() {
      let endpoint = "api/seans/";
      apiService(endpoint).then(data => {
        this.seans_table2.push(...data);
      });
    },
    pick_seans(seans) {
      this.pickedSeansID = seans;
      let tabel = new Array();
      this.tickets.forEach(ticket => {
        if (ticket.seans_name === seans.id) {
          tabel.push(ticket);
        }
      });
      this.reserved = tabel;
    }
  }
};
</script>

<style scoped></style>
