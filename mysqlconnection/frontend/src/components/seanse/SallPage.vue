<template>
  <v-container>
    Wybrany seans: {{ SeansIDnew }} <br />
    Wybrany film: {{ film }}<br />
    wybrana sala: {{ sall }}<br />
    {{ SeansIDnew.seans_id }}<br />

    Miejsca zarezerwowane: {{ Reserved_tabel }}

    <!--    {{ Seans }}-->
    <v-row align-content="center" justify="center">
      <v-card align="center" class="pa-2">
        <div class="rectangle">EKRAN</div>
        <template v-if="Reserved_tabel">
          <v-layout v-for="Row in sall.liczba_rzedow" :key="Row">
            <FpToggle
              :lay="get_letter_by_id(Row - 1)"
              :places="sall.liczba_kolumn"
              @bind_methods="SetTable"
              :reserved="Reserved_tabel"
            ></FpToggle>
          </v-layout>
        </template>
        <!--        <v-btn @click="showTable">CHECK</v-btn>-->
        <v-btn @click="AddTicket">KUP BILETY</v-btn>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
import FpToggle from "@/FPcomponents/FpToggle.vue";
import { apiService } from "@/common/api.service";

export default {
  name: "SallPage",
  components: { FpToggle },
  props: ["Sala", "Seans", "SeansIDnew"],
  data: () => ({
    tabel_choesen_seats: [],
    sall: [],
    film: [],
    tickets1: [],
    Reserved_tabel: []
  }),
  mounted() {
    this.getFilm();
    this.getSall();
    this.MakeArray();
    this.getReservedTable();

    // this.MakeNewArray();
  },
  watch: {
    SeansIDnew: {
      deep: true,
      handler() {
        this.getFilm();
        this.getSall();
        this.getReservedTable();
      }
    }
  },

  methods: {
    getFilm() {
      let endpoint = `api/films/${this.SeansIDnew.film}/`;
      apiService(endpoint).then(data => {
        this.film = data;
      });
    },
    getSall() {
      let endpoint = `api/sall/${this.SeansIDnew.sala}/`;
      console.log(endpoint);
      apiService(endpoint).then(data => {
        this.sall = data;
      });
    },
    getReservedTable() {
      let endpoint = `api/reserved/`;
      let reserveds = [];
      apiService(endpoint).then(data => {
        data.forEach(place => {
          if (place.seans === this.SeansIDnew.seans_id) {
            const x = place.adres_miejsca.split("-");
            console.log(x);
            reserveds.push({ row: x[0], column: parseInt(x[1]) });
          }
        });
        this.Reserved_tabel = reserveds;
      });
    },

    MakeArray() {
      this.tabel_choesen_seats = new Array(this.Sala.rows);
    },
    makeReservePlaces() {},
    // MakeNewArray() {
    //     this.tabel_choesen_seats = new Array(this.sall.number_of_rows);
    // },
    get_letter_by_id(id) {
      return String.fromCharCode(65 + id);
    },
    showTable() {
      console.log(this.tabel_choesen_seats);
    },
    SetTable(e, y) {
      let newArray = new Array();
      newArray = this.tabel_choesen_seats;
      let row = y.charCodeAt();
      row = row - 65;
      newArray[row] = { miejsca: e };
      this.tabel_choesen_seats = newArray;
    },
    AddTicket() {
      const newTicket = {
        seans: this.SeansIDnew,
        film_name: this.film.title,
        miejsca: this.tabel_choesen_seats
      };
      this.$store.commit("addTicketToCart", newTicket);
      this.$router.push({
        path: "/ticket"
      });
    }
  }
};
</script>

<style scoped>
.rectangle {
  width: 60%;
  background-color: lightgrey;
  text-align: center;
  margin: auto;
}
</style>
