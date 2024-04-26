<template>
  <div class="bg-background w-full min-h-screen duration-500">
    <div class="flex justify-center">
      <TextToAudioWindow :speakers="speakers" :languages="languages" />
    </div>
  </div>
</template>

<script>

import Header2 from "@/components/Header2.vue";
import Footer from "@/components/Footer.vue";
import TextToAudioWindow from "../components/TextToAudioWindow.vue";
import ErrorPage from "@/components/ErrorPage.vue";
import LoaderBig from "@/components/LoaderBig.vue";

export default {
  components: {
    Header2,
    Footer,
    TextToAudioWindow,
    ErrorPage,
    LoaderBig,
  },
};
</script>

<style></style>
