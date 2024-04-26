<template>
  <span :class="[isDarkMode ? 'loader-dark' : 'loader-light']"></span>
  <div>
    <AnimatedText />
  </div>
</template>
<script>
import AnimatedText from "./AnimatedText.vue";

export default {
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  components: { AnimatedText },
};
</script>
<style scoped>
.loader-light {
  position: relative;
  width: 120px;
  height: 55px;
  background-repeat: no-repeat;
  background-image: radial-gradient(circle 2.5px, #ee0000 100%, transparent 0),
    linear-gradient(#eee 90px, transparent 0),
    linear-gradient(#4d4d4d 120px, transparent 0),
    linear-gradient(to right, #333 10%, #eee 10%, #eee 90%, #333 90%);

  background-size: 5px 5px, 90px 10px, 120px 45px, 100px 15px;
  background-position: 110px 15px, center bottom, center bottom, center 0;
}
.loader-light:before {
  content: "";
  width: 70px;
  background-color: #bbb;
  box-shadow: 0 0 10px #3c3c3c00;
  position: absolute;
  left: 50%;
  transform: translatex(-50%);
  bottom: calc(100% - 10px);
  animation: printerPaper 4s ease-in infinite;
}
.loader-light:after {
  content: "";
  width: 70px;
  height: 80px;
  background-color: #505050;
  background-image: linear-gradient(to bottom, #505050 50%, #ffffff 51%),
    linear-gradient(to bottom, #fff 50%, #505050 51%);
  background-size: 60px 20px, 60px 10px;
  background-repeat: no-repeat, repeat-y;
  background-position: center 55px, center 0;
  position: absolute;
  left: 50%;
  transform: translatex(-50%) rotate(180deg);
  box-shadow: 0 10px #505050 inset;
  top: calc(100% - 8px);
  animation: PrintedPaper 4s ease-in infinite;
}
.loader-dark {
  position: relative;
  width: 120px;
  height: 55px;
  background-repeat: no-repeat;
  background-image: radial-gradient(circle 2.5px, #ff3d00 100%, transparent 0),
    linear-gradient(#525252 90px, transparent 0),
    linear-gradient(#ececec 120px, transparent 0),
    linear-gradient(to right, #eee 10%, #333 10%, #333 90%, #eee 90%);

  background-size: 5px 5px, 90px 10px, 120px 45px, 100px 15px;
  background-position: 110px 15px, center bottom, center bottom, center 0;
}
.loader-dark:before {
  content: "";
  width: 70px;
  background-color: #fff;
  box-shadow: 0 0 10px #0003;
  position: absolute;
  left: 50%;
  transform: translatex(-50%);
  bottom: calc(100% - 10px);
  animation: printerPaper 4s ease-in infinite;
}
.loader-dark:after {
  content: "";
  width: 70px;
  height: 80px;
  background-color: #fff;
  background-image: linear-gradient(to bottom, #fff 50%, #ff3d00 51%),
    linear-gradient(to bottom, #bbb 50%, #0000 51%);
  background-size: 60px 20px, 60px 10px;
  background-repeat: no-repeat, repeat-y;
  background-position: center 55px, center 0;
  position: absolute;
  left: 50%;
  transform: translatex(-50%) rotate(180deg);
  box-shadow: 0 10px #fff inset;
  top: calc(100% - 8px);
  animation: PrintedPaper 4s ease-in infinite;
}
@keyframes printerPaper {
  0%,
  25% {
    height: 50px;
  }
  75%,
  100% {
    height: 0;
  }
}

@keyframes PrintedPaper {
  0%,
  30% {
    height: 0px;
    top: calc(100% - 8px);
  }

  80% {
    height: 80px;
    top: calc(100% - 8px);
    opacity: 1;
  }
  100% {
    height: 80px;
    top: calc(100% + 10px);
    opacity: 0;
  }
}
</style>
