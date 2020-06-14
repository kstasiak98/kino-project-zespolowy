import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    cart: [],
    userOnline: {},
    ifLogin: false,
    FullPrize: 0
  },
  mutations: {
    addTicketArrayToCart(state, ticketArray) {
      ticketArray.forEach(ticket => state.cart.push(ticket));
    },
    addTicketToCart(state, ticket) {
      state.cart.push(ticket);
    },
    removeTicketFromCart(state) {
      state.cart.pop();
    },
    setUser(state, user) {
      state.userOnline = {
        login: user.login,
        id: user.id,
        email: user.email,
        punkty: user.punkty
      };
      state.ifLogin = true;
      console.log(state);
    }
  },
  actions: {},
  modules: {}
});
