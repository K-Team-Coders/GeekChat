<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-screen">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="ml-72 w-5/6 outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <div class=" w-full px-2 uppercase text-activeText font-rale font-bold  mt-4 text-center text-4xl">
        Список сессий
      </div>

      <router-link to="/chat">
      <div class="px-2 uppercase text-activeText font-rale font-bold  mt-4  mx-48 rounded-lg">
        <div class="flex flex-row dark:bg-slate-500 bg-slate-200 dark:hover:bg-slate-700 hover:bg-slate-500 duration-300">
          <div class="p-4 w-full">
            <p class="text-2xl text-start">1. Сессия № 1</p>
          </div> 
          <button class="hover:cursor-pointer hover:bg-indigo-700 duration-300 w-full ml-96 text-center bg-indigo-400 font-rale">Перейти</button>
        </div>
      </div>
    </router-link>
    
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import AssistantCategoryService from "./AssistantCategoryService.vue";
import AssistantCategoryServiceSection from "./AssistantCategoryServiceSection.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
export default {
  components: {
    AssistantCategoryService,
    BaseIcon,
    AssistantCategoryServiceSection,
    SidebarMain,
  },

  data() {
    return {
      questionQuery: '',
    }
  },

  methods: {
    askQuestion() {
      console.log(this.questionQuery)
      axios.post(`http://${process.env.VUE_APP_ASSISTANT_SEARCH_IP}/assistant/llamaSupportStream?text=${this.questionQuery}`, { responseType: 'stream' },
      )
        .then(response => {
          console.log(response.data)
        })
    }
  },

  computed: {
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
  animation: fly-around 5s ease-in-out infinite;
}

@keyframes fly-around {
  0% {
    left: 40px;
    top: 0px;
  }

  25% {
    left: 40px;
    top: 20px;
  }

  50% {
    left: 55px;
    top: 5px;
  }

  75% {
    left: 25;
    top: 15px;
  }

  100% {
    left: 40px;
    top: 0px;
  }
}

.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #535353;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #323232;
}
</style>
