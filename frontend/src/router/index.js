import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "allservices",

    component: () => import("../views/ChatList.vue"),
  },

  {
    path: "/dashboards",
    name: "Dashboards",

    component: () => import("../views/Dashboards.vue"),
  },
  {
    path: "/notfound",
    name: "NotFound",
    component: () => import("../components/PageNotFound.vue"),
    props: true,
  },
  {
    path: "/chat",
    name: "Chat",
    component: () => import("../views/SessionChat.vue"),
    props: true,
  },

  {
    path: "/admin_session",
    name: "admin_session",
    component: () => import("../components/OneSessionWindow.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
