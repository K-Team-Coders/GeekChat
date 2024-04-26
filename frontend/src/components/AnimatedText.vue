<template>
  <div class="pl-5 pt-6" :class="[isDarkMode ? 'waviy-dark' : 'waviy-light']">
    <span style="--i: 1">З</span>
    <span style="--i: 2">А</span>
    <span style="--i: 3">Г</span>
    <span style="--i: 4">Р</span>
    <span style="--i: 5">У</span>
    <span style="--i: 6">З</span>
    <span style="--i: 7">К</span>
    <span style="--i: 8">А</span>
    <span style="--i: 9">.</span>
    <span style="--i: 10">.</span>
    <span style="--i: 11">.</span>
  </div>
</template>
<script>
export default {
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
};
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Alfa+Slab+One&display=swap");
.waviy-light {
  position: relative;
  -webkit-box-reflect: below -20px linear-gradient(transparent, rgba(0, 0, 0, 0.2));
  font-size: 30px;
}
.waviy-light span {
  font-family: "Alfa Slab One", cursive;
  position: relative;
  display: inline-block;
  color: #000000;
  text-transform: uppercase;
  animation: waviy 1s infinite;
  animation-delay: calc(0.1s * var(--i));
}
.waviy-dark {
  position: relative;
  -webkit-box-reflect: below -20px linear-gradient(transparent, rgba(0, 0, 0, 0.2));
  font-size: 30px;
}
.waviy-dark span {
  font-family: "Alfa Slab One", cursive;
  position: relative;
  display: inline-block;
  color: #fff;
  text-transform: uppercase;
  animation: waviy 1s infinite;
  animation-delay: calc(0.1s * var(--i));
}
@keyframes waviy {
  0%,
  40%,
  100% {
    transform: translateY(0);
  }
  20% {
    transform: translateY(-20px);
  }
}
</style>
