<template>
  <div class="flex flex-col gap-2 min-h-screen relative duration-500">
    <router-link to="/">
      <div class="">
        <div class="absolute -left-[13px] -top-4 z-10 duration-500">
          <span class="duration-500">
            <svg
              width="275"
              height="90"
              class="duration-500"
              stroke=""
              xmlns="http://www.w3.org/2000/svg"
              xmlns:svg="http://www.w3.org/2000/svg"
            >
              <g>
                <g id="svg_8">
                  <g id="svg_6">
                    <path
                      id="svg_2"
                      d="m30.332,35.697l20.379,54.084l0,-51.097l-20.379,-2.987l0,0z"
                      :style="{ fill: isDarkMode ? 'white' : 'black' }"
                      stroke-width="14"
                    />
                    <path
                      stroke="null"
                      id="svg_3"
                      d="m25.993,38.37l13.561,35.045l-20.875,-14.008l-4.87,-19.332l12.184,-1.705m1.265,-2.153l-15.879,2.223l5.585,22.172l26.655,17.888l-16.361,-42.283l0,0z"
                      :style="{ fill: isDarkMode ? 'white' : 'black' }"
                      stroke-width="14"
                    />
                    <path
                      stroke="null"
                      id="svg_4"
                      d="m50.724,0l-20.289,5.869l-20.29,-5.869l-10.145,17.571l10.145,17.57l20.289,-2.608l20.29,2.608l10.144,-17.57l-10.144,-17.571zm-1.848,26.283l-9.973,-0.896l-2.24,-3.521l1.114,-1.725l2.199,3.472l7.882,0.708l3.897,-6.75l-3.866,-6.696l-7.899,1.456l-9.556,17.959l-9.557,-17.96l-7.899,-1.455l-3.865,6.696l3.896,6.75l7.883,-0.708l2.215,-3.458l1.111,1.712l-2.255,3.521l-9.973,0.896l-5.028,-8.712l5.06,-8.766l9.938,1.831l8.474,15.795l8.474,-15.796l9.938,-1.831l5.062,8.766l-5.032,8.712zm-8.936,-8.223l1.88,-3.041l4.066,-0.393l1.984,3.434l-1.984,3.434l-3.965,-0.279l-1.981,-3.155zm-19.01,0l-1.984,3.154l-3.964,0.279l-1.982,-3.434l1.982,-3.434l3.863,0.393l2.085,3.042z"
                      :style="{ fill: isDarkMode ? 'white' : 'black' }"
                      stroke-width="14"
                    />
                  </g>
                </g>
              </g>
            </svg>
          </span>
        </div>
        <p
          class="text-activeText text-8xl text-center rainbows z-20 font-stengazeta -mb-5 duration-500"
        >
          СОВА
        </p>
        <p
          class="text-base z-30 font-stengazeta text-center text-activeText duration-500"
        >
          интеллектуальный помощник
        </p>
      </div>
    </router-link>
    <div class="flex flex-col justify-between h-full w-full pt-1 duration-500">
      <div class="w-full flex flex-col gap-2">
        <AssistantCategoryServiceSection>
          <router-link
            v-for="service in services"
            :key="service.name"
            :to="service.route"
          >
            <AssistantCategoryService
              :category="service.category"
              :name="service.name"
              :classed="service.classed"
              :isActive="service.isActive"
            />
          </router-link>
        </AssistantCategoryServiceSection>
      </div>
      <div class="flex justify-center w-full absolute bottom-8">
        <Switcher />
      </div>
    </div>
  </div>
</template>
<script>
import AssistantCategoryService from "./AssistantCategoryService.vue";
import AssistantCategoryServiceSection from "./AssistantCategoryServiceSection.vue";
import BaseIcon from "./BaseIcon.vue";
import Switcher from "./Switcher.vue";
export default {
  components: {
    AssistantCategoryService,
    AssistantCategoryServiceSection,
    BaseIcon,
    Switcher,
  },

  computed: {
    services() {
      return [
        {
          category: "Чат",
          name: "chat",
          classed: "w-8 h-8 text-blue-400",
          route: "/assistant",
          isActive: this.$route.path === "/assistant",
        },
        {
          category: "Переводчик",
          name: "translate",
          classed: "w-8 h-8 text-yellow-400",
          route: "/translater",
          isActive: this.$route.path === "/translater",
        },
        {
          category: "Распознать текст",
          name: "eye",
          classed: "w-8 h-8 text-purple-400",
          route: "/scan_from_docs",
          isActive: this.$route.path === "/scan_from_docs",
        },
        {
          category: "Поиск документов",
          name: "search",
          classed: "w-8 h-8 text-green-400",
          route: "/search_document",
          isActive: this.$route.path === "/search_document",
        },
        {
          category: "Распознать аудио",
          name: "microphone",
          classed: "w-8 h-8 text-red-700",
          route: "/audio_recognition",
          isActive: this.$route.path === "/audio_recognition",
        },
        {
          category: "Преобразовать в аудио",
          name: "gromko",
          classed: "w-8 h-8 text-orange-400",
          route: "/text_to_audio",
          isActive: this.$route.path === "/text_to_audio",
        },
        {
          category: "Распознать объект",
          name: "flag",
          classed: "w-8 h-8 text-red-400",
          route: "/image_recognition",
          isActive: this.$route.path === "/image_recognition",
        },
        {
          category: "Сформировать документ",
          name: "news",
          classed: "w-8 h-8 text-green-200",
          route: "/2",
          isActive: this.$route.path === "/2",
        },
        {
          category: "Поиск",
          name: "viewgrid",
          classed: "w-8 h-8 text-activeText duration-500",
          route: "/",
          isActive: this.$route.path === "/",
        },
      ];
    },
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
};
</script>
<style>
.rainbows {
  position: relative;
}
@keyframes rainbow {
  0% {
    color: white;
  }
  33% {
    color: blue;
  }
  66% {
    color: red;
  }
  100% {
    color: white;
  }
}
.owl {
  position: absolute;
  width: 40px;
  height: 40px;
  background-image: url("https://freesvg.org/img/1531730612.png");
  background-size: cover;
  animation: fly-around 12s ease-in-out infinite;
}

@keyframes fly-around {
  0% {
    left: 10%;
    top: -3%;
  }
  25% {
    left: 23%;
    top: 2%;
  }
  50% {
    left: 60%;
    top: 1%;
  }
  75% {
    left: 75%;
    top: -3%;
  }
  100% {
    left: 10%;
    top: -3%;
  }
}
</style>
