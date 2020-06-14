<template>
  <v-container>
    <!--    <v-row>-->
    <!--      <v-col cols="3" class="film-column" v-for="film in films1" :key="film.id">-->
    <!--        <FilmPage :filmP="film"></FilmPage>-->
    <!--      </v-col>-->
    <!--    </v-row>-->
    <v-row>
      <!--      {{newFilms}}-->
      <v-col
        cols="3"
        class="film-column"
        v-for="film in newFilms"
        :key="film.id"
      >
        <FilmPage :filmP="film"></FilmPage>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FilmPage from "./FilmPage.vue";
import { FILMS } from "@/components/DATA/database";
import { apiService } from "@/common/api.service";

export default {
  name: "RepertoirePage",
  components: { FilmPage },
  data() {
    return {
      films1: FILMS,
      newFilms: []
    };
  },
  methods: {
    getFilms() {
      let endpoint = "api/films/";
      apiService(endpoint).then(data => {
        this.newFilms.push(...data);
      });
    }
  },
  created() {
    this.getFilms();
    console.log(this.newFilms);
  }
};
</script>

<style scoped>
.film-column {
  justify-content: center;
  text-align: center;
  flex-wrap: wrap !important;
}
</style>
