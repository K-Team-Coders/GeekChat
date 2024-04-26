<template>
  <div class="bg-background min-h-screen w-full duration-500">
    <div class="flex justify-center">
      <AudioRecognitionWindow />
    </div>
  </div>
</template>

<script>
import Header2 from "@/components/Header2.vue";
import Footer from "@/components/Footer.vue";
import AudioRecognitionWindow from "@/components/AudioRecognitionWindow.vue";

export default {
  components: {
    Header2,
    Footer,
    AudioRecognitionWindow,
  },
};
</script>

<style></style>
