<template>
  <div class="flex justify-center pt-10">
    <vue-word-cloud
      style="height: 300px; width: 800px"
      :words="words"
      :animation-duration="1000"
      :animation-easing="ease"
      :animation-overlap="1/5"
      :spacing = 0.2
      :color="
        ([, weight]) =>
          weight > 4 ? '#00cf00' : weight > 1 ? 'red' : 'neutral-100'
      "
      font-family="Geologica"
    >
  </vue-word-cloud>
  </div>
</template>

<script>
import VueWordCloud from "vuewordcloud";

export default {
  components: {
    [VueWordCloud.name]: VueWordCloud,
  },
  props: {
    words: Object,
    wordcolors: Object
  },
  mounted(){
   
    // let text_color_list = []
    // let unit_answer = []
    // wordcolors.forEach(element => {
      
      
    // });
  }
};
</script>

<style></style>
