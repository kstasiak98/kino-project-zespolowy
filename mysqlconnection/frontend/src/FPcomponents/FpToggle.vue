<template>
  <v-layout>
    <v-col>
      <b>{{ this.lay }}: </b>
      <v-btn-toggle v-model="toggle_follow" multiple>
        <template v-for="(place, index) in places">
          <FpButton
            v-bind:key="place"
            :buttonN="index + 1"
            :if-disable="disable_buton(index + 1)"
          ></FpButton>
        </template>
      </v-btn-toggle>
    </v-col>
  </v-layout>
</template>
<script>
import FpButton from "./FpButton.vue";
import { SALA_MIEJSCA } from "@/components/DATA/database";

export default {
  name: "FpToggle",
  components: { FpButton },
  props: ["lay", "places", "reserved"],
  data() {
    return {
      Sall: SALA_MIEJSCA[0].columns,
      toggle_follow: []
    };
  },
  watch: {
    toggle_follow: {
      deep: true,
      handler() {
        if (this.bind_methods()) {
          this.bind_methods();
        }
      }
    }
  },
  computed: {
    make_array() {
      const array = [];
      if (this.toggle_follow) {
        for (let i = 0; i < this.toggle_follow.length; i += 1) {
          const place1 = `${this.lay}-${this.toggle_follow[i] + 1}`;
          const place = {
            number: this.toggle_follow[i] + 1,
            lay: this.lay,
            code: place1
          };
          array.push(place);
        }
      }
      return array;
    }
  },
  methods: {
    bind_methods() {
      this.$emit("bind_methods", this.make_array, this.lay);
    },
      disable_buton(value) {
          for (let i = 0; i < this.reserved.length; i = i + 1) {
              if (this.lay === this.reserved[i].row && value === this.reserved[i].column) {
                  return false
              }
          }
          return value !== 0;
        },
  }
};
</script>
<style scoped lang="scss"></style>
