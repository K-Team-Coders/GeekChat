<template>
  <div class="bg-background w-full duration-500 min-h-[100vh]">
    <div class="flex justify-center">
      <ImageRecognitionWindow />
    </div>
  </div>
</template>

<script>
import Header2 from "@/components/Header2.vue";
import Footer from "@/components/Footer.vue";
import ImageRecognitionWindow from "@/components/ImageRecognitionWindow.vue";

export default {
  components: {
    Header2,
    Footer,
    ImageRecognitionWindow,
  },
};
</script>

<style></style>
