import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/Home/HomeView.vue";
import Ridam from "../views/ridam-management-module/ridam.vue";
import PrimaryDataManagement from "../views/ridam-management-module/primary-data-management/primary-data-management.vue";
import PDMainPage from "../views/ridam-management-module/primary-data-management/Primary-data-main-page.vue";
import About from "../views/Home/help/AboutView.vue";
import edit from "../views/ridam-management-module/primary-data-management/edit.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: About,
  },
  {
    path: "/ridam",
    name: "Ridam",
    component: Ridam,
  },
  {
    path: "/primary-data-management",
    name: "pdm",
    component: PrimaryDataManagement,
  },
  {
    path: "/Primary-data-main-page",
    name: "pdm-main",
    component: PDMainPage,
  },
  {
    path: "/edit/:id",
    name: "edit",
    component: edit,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
