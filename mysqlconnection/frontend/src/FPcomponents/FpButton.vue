<template>
  <v-btn
    v-if="ifDisable"
    class="miejsce"
    height="48px"
    min-width="48px"
    elevation="0"
    @click="type = !type"
    :color="type === false ? '#76FF03' : '#f5f5f5'"
    >{{ buttonN }}
  </v-btn>
  <v-btn
    v-else
    class="miejsce"
    height="48px"
    min-width="48px"
    elevation="0"
    disabled
    >{{ buttonN }}
  </v-btn>
</template>

<script>
export default {
  name: "FpButton",
  props: {
    buttonN: Number,
    ifDisable: Boolean
  },
  data() {
    return {
      czyTak: true,
      type: true
    };
  }
};
</script>

<style scoped lang="scss">
.miejsce {
  border-color: rgba(0, 0, 0, 0.12) !important;
  border-style: solid;
  border-width: thin;
  border-radius: 0;
  opacity: 0.8;
  padding: 0 12px;
  box-shadow: none;
}
</style>
