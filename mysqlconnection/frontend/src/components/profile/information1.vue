<template>
  <v-row>
    <v-col>
      <p>Zarejestrowałeś się pomyślnie</p><br/>
    </v-col>
    <v-col>
      <v-btn @click="back()">BACK</v-btn>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name: 'information1',
  methods: {
    back() {
      this.$router.push('/login');
    },
  },
};
</script>
<style scoped lang="scss">
</style>
