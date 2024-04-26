import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "allservices",

    component: () => import("../views/MainPage.vue"),
  },

  {
    path: "/assistant",
    name: "Assistant",

    component: () => import("../views/ChatList.vue"),
  },
  {
    path: "/notfound",
    name: "NotFound",
    component: () => import("../components/PageNotFound.vue"),
    props: true,
  },
  {
    path: "/chat",
    name: "NotFound",
    component: () => import("../views/SessionChat.vue"),
    props: true,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
