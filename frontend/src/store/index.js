import { createStore } from "vuex";

export default createStore({
  state: {
    darkMode: JSON.parse(localStorage.getItem("darkMode")) || false,
  },
  mutations: {
    toggleDarkMode(state) {
      state.darkMode = !state.darkMode;
      localStorage.setItem("darkMode", state.darkMode);
    },
  },
  actions: {
    toggleDarkMode({ commit }) {
      commit("toggleDarkMode");
    },
  },
});