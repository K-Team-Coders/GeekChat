<template>
  <div class="bg-background w-full min-h-screen duration-500">
    <div class="flex justify-center">
      <TransleterWindow :origin_languages="origin_languages" />
    </div>
  </div>
</template>

<script>
import Header2 from "@/components/Header2.vue";
import Footer from "@/components/Footer.vue";
import TransleterWindow from "../components/TransleterWindow.vue";

export default {
  components: {
    Header2,
    TransleterWindow,
    Footer,
  },
};
</script>

<style></style>
