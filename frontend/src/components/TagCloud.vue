<template>
  <div class="backbody flex flex-col rounded-2xl w-full justify-center">
    <div class="xl:flex flex-row sm:px-40 px-4 gap-4 justify-center">
      <div class="bg-neutral-100 rounded-xl p-4 sm:max-w-[450px] w-full mx-auto">
        <BarChart :dataset="result.clusters" />
      </div>
      <div
        class="sm:bg-neutral-100 flex justify-center rounded-xl p-4 lg:max-w-2xl sm:max-w-[450px] min-w-[450px] sm:mx-auto"
      >
        <span ref="tagcloud--item" class="Sphere cursor-pointer"></span>
      </div>
      <div
        class="bg-neutral-100 rounded-xl sm:p-4 p-10 lg:max-w-2xl sm:mx-auto sm:max-w-[450px]"
      >
        <Doughnut
          :dataset="[
            result.totalPositive,
            result.totalNeutral,
            result.totalNegative,
          ]"
        ></Doughnut>
      </div>
    </div>
    <div
      v-if="isOpened"
      class="flex flex-col pt-10 px-6 justify-center text-center"
    >
      <p class="bg-idealblack text-activeText font-bold sm:text-3xl">
        Кластер: {{ texts }}
      </p>
      <WordCloud :wordcolors="this.text_colors" :words="this.text_list" />
    </div>
  </div>
</template>

<script>
import TagCloud from "TagCloud";
import WordCloud from "@/components/WordCloud.vue";
import BarChart from "@/components/charts/BarChart.vue";
import Doughnut from "@/components/charts/Doughnut.vue";

export default {
  components: { TagCloud, WordCloud, BarChart, Doughnut },
  data() {
    return {
      texts: "nothing",
      isOpened: false,
      text_colors: [],
      text_list: [],
    };
  },

  props: {
    result: Object,
  },
  methods: {
    onClick(e) {
      this.isOpened = true;
      if (e.target.className === "tagcloud--item") {
        this.texts = e.target.innerText;
        let id = this.getClustersName().indexOf(this.texts);
        this.text_list = this.result.clusters[id].tagCloud;
        this.text_colors = this.result.clusters[id].wordsSentiment;
      }
    },
    getClustersName() {
      const cluster_list = []
      
      this.result.clusters.forEach((element) => cluster_list.push(element.cluster_name));
  
      return cluster_list
    }
  },

  mounted() {
   
    const Texts = this.getClustersName()
    
    let tagCloud = TagCloud(".Sphere", Texts, {
      radius: 230,

      maxSpeed: "fast",
      initSpeed: "fast",

      direction: 135,

      keep: true,
    });

    let color = "#544adde1";
    document.querySelector(".Sphere").style.color = color;

    let element = this.$refs["tagcloud--item"];
    element.addEventListener("click", this.onClick);
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");

.backbody {
  background-color: #222;
}

.tagcloud {
  display: inline-block;
  font-weight: bold;
  letter-spacing: 1px;
  font-family: "Roboto", italic;
  font-size: 20px;
}

.tagcloud--item:hover {
  color: rgb(153, 32, 32);
}
</style>
