import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import HomeView2 from "@/views/HomeView2.vue";
import AddTransaction from "@/views/AddTransaction.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      // beforeEnter: (to, from, next) => {
      //   const token = getCookie("token");
      //   if (token) {
      //     next();
      //   } else {
      //     next({ name: "login" });
      //   }
      // },
      // beforeEnter: (to, from) => {
      //   // reject the navigation
      //   const token = getCookie("token");
      //   if (!token) {
      //     return false
      //   }
        
      // },
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/home_2",
      name: "home_2",
      component: HomeView2,
    },
    {
      path: "/add-transaction",
      name: "add-transaction",
      component: AddTransaction,
    }
  ],
});

export default router;
