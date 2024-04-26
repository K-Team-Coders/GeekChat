<template>
  <div :class="themeClass">
    <router-view />
    <Switcher @toggle-dark-mode="toggleDarkMode" class="hidden"></Switcher>
  </div>
</template>
<script>
import Switcher from "./components/Switcher";
import { mapState, mapActions } from "vuex";

export default {
  components: {
    Switcher,
  },
  computed: {
    ...mapState(["darkMode"]),
    themeClass() {
      return {
        light: !this.darkMode,
        dark: this.darkMode,
      };
    },
  },
  methods: {
    ...mapActions(["toggleDarkMode"]),
  },
};
</script>
