import Vue from "vue";
import Router from "vue-router";
import HomePage from "../components/HelloWorld.vue";
import RepertoirePage from "@/components/films/RepertoirePage";
import ShopPage from "@/components/seanse/ShopPage";
import TicketPage from "@/components/shop/TicketPage";
import LoginPage from "@/components/profile/LoginPage";
import ProfilePage from "@/components/profile/ProfilePage";
import information1 from "@/components/profile/information1";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomePage
    },
    {
      path: "/repertoire",
      name: "Repertoire",
      component: RepertoirePage
    },
    {
      path: "/store",
      name: "Store",
      component: ShopPage
    },
    {
      path: "/ticket",
      name: "Ticket",
      component: TicketPage
    },
    {
      path: "/login",
      name: "Login",
      component: LoginPage
    },
    {
      path: "/login/profile",
      name: "Profile",
      component: ProfilePage
    },
    {
      path: "/information",
      name: "information",
      component: information1
    }
  ]
});
