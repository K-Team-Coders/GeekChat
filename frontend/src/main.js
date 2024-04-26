import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./index.css";
import Vuex from "vuex";
store.dispatch("loadDarkMode");
createApp(App).use(store).use(router).use(Vuex).mount("#app");