<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-screen">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div class="ml-72 w-4/6 outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <div class="h-full px-2">

        <div class="relative h-full flex justify-center">
          <!-- Блок ответов -->
          <div class="h-[85vh] overflow-y-auto p-16 w-full mb-16">
            <!-- Входящее сообщение -->
            <div class="flex mb-4 cursor-pointer">
              <div class="w-9 h-9 rounded-full flex items-center justify-center mr-2">
                <img src="@/img/sova.jpg" alt="User Avatar"
                  class="w-12 h-12 rounded-full">
              </div>
              <div class="flex max-w-96 bg-white rounded-lg p-3 gap-3 outline">
                <p class="text-gray-700">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Delectus est pariatur tenetur sint, animi vitae debitis! Voluptatem qui ducimus doloribus assumenda similique natus, eius, amet eaque ex ratione dolorem ut.</p>
              </div>
            </div>

            <!-- Исходящее сообщение -->
            <div class="flex justify-end mb-4 cursor-pointer">
              <div class="flex max-w-96 bg-indigo-500 text-white rounded-lg p-3 gap-3">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi mollitia minus obcaecati ullam deleniti repellendus officia at labore atque sequi ad laborum nesciunt suscipit, ut illo modi error sit expedita!</p>
              </div>
              <div class="w-9 h-9 rounded-full flex items-center justify-center ml-2">
                <img src="https://placehold.co/200x/b7a8ff/ffffff.svg?text=Я&font=Lato" alt="My Avatar"
                  class="w-8 h-8 rounded-full">
              </div>
            </div>

            <div class="flex mb-4 cursor-pointer">
              <div class="w-9 h-9 rounded-full flex items-center justify-center mr-2">
                <img src="@/img/sova.jpg" alt="User Avatar"
                  class="w-12 h-12 rounded-full">
              </div>
              <div class="flex max-w-96 bg-white rounded-lg p-3 gap-3 outline">
                <p class="text-gray-700">Lorem ipsum dolor sit, amet consectetur adipisicing elit. Delectus est pariatur tenetur sint, animi vitae debitis! Voluptatem qui ducimus doloribus assumenda similique natus, eius, amet eaque ex ratione dolorem ut.</p>
              </div>
            </div>

            <!-- Исходящее сообщение -->
            <div class="flex justify-end mb-4 cursor-pointer">
              <div class="flex max-w-96 bg-indigo-500 text-white rounded-lg p-3 gap-3">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Eligendi mollitia minus obcaecati ullam deleniti repellendus officia at labore atque sequi ad laborum nesciunt suscipit, ut illo modi error sit expedita!</p>
              </div>
              <div class="w-9 h-9 rounded-full flex items-center justify-center ml-2">
                <img src="https://placehold.co/200x/b7a8ff/ffffff.svg?text=Я&font=Lato" alt="My Avatar"
                  class="w-8 h-8 rounded-full">
              </div>
            </div>
            
          </div>
          

          <div class="absolute bottom-3 w-full flex items-center gap-2 justify-center px-2">
            <input v-model="questionQuery"
              class="w-11/12 rounded-xl h-10 border-[1.5px] bg-transparent px-4 text-activeText placeholder:text-unactiveText border-neutral-500 dark:border-neutral-200 duration-500"
              type="text" placeholder="Спрашивайте все, что угодно..." />
            <input class="hidden" aria-describedby="file_input_help" id="files" ref="allFiles" type="file" accept="" />
            <button class="items-center flex justify-center" @click="$refs.allFiles.click()"
              :style="{ fill: isDarkMode ? 'white' : 'black' }">
              <svg version="1.1" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                class="w-6 h-6 ml-[3px]" viewBox="0 0 30.58 30.58" xml:space="preserve">
                <g>
                  <path style="dark:fill: #ffffff fill:#000000"
                    d="M28.692,3.179c-1.892-1.892-4.867-3.428-8.295,0L6.5,17.075c-0.107,0.096-1.386,1.297-1.431,3.039 c-0.028,1.076,0.413,2.079,1.313,2.979c0.768,0.768,1.687,1.167,2.655,1.155c1.754-0.021,3.062-1.343,3.204-1.493l10.455-10.454 c0.391-0.391,0.392-1.023,0-1.414c-0.391-0.391-1.023-0.391-1.414,0L10.811,21.358c-0.249,0.256-1.029,0.884-1.807,0.89 c-0.426,0.003-0.821-0.184-1.208-0.57c-0.5-0.5-0.738-0.99-0.728-1.501c0.017-0.907,0.805-1.647,0.813-1.656l13.93-13.928 c1.352-1.351,3.059-2.409,5.467,0c0.882,0.882,1.319,1.796,1.302,2.718c-0.029,1.515-1.257,2.667-1.27,2.679L11.691,25.434 c-0.034,0.034-1.965,1.986-4.316,2.002c-1.237,0.008-2.412-0.536-3.492-1.615c-4.082-4.082-0.262-8.156-0.098-8.327L15.798,5.48 c0.391-0.391,0.391-1.023,0-1.415c-0.392-0.391-1.024-0.39-1.414,0L2.356,16.093c-1.878,1.956-4.249,6.78,0.112,11.142 c1.478,1.477,3.139,2.217,4.937,2.2c3.198-0.028,5.608-2.491,5.709-2.596l15.574-15.4c0.044-0.039,1.832-1.686,1.891-4.064 C30.616,5.879,29.981,4.467,28.692,3.179z" />
                </g>
              </svg>
            </button>
            <button @click="askQuestion()">
              <svg :style="{ fill: isDarkMode ? 'white' : 'black' }" class="w-7 h-7" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M4.10514201,11.8070619 L2.74013818,2.2520351 L22.236068,12 L2.74013818,21.7479649 L4.10514201,12.1929381 L4.87689437,12 L4.10514201,11.8070619 Z M5.25986182,5.7479649 L5.89485799,10.1929381 L13.1231056,12 L5.89485799,13.8070619 L5.25986182,18.2520351 L17.763932,12 L5.25986182,5.7479649 Z" />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>
    <!-- Блок истории запросов -->
    <!-- <div class="w-1/6 outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <div class="min-h-full p-3">
        <p class="text-activeText py-2 text-center rounded-xl mb-4 text-xl font-medium duration-500">
          История запросов
        </p>
        <div class="w-full px-2 overflow-y-scroll h-[80vh] custom-scrollbar duration-500">
          <div v-for="i in 40" class="text-activeText pt-2 w-full duration-500">
            <div class="border-2 rounded-xl px-3 py-3 flex relative items-center hover:bg-hoverBackground duration-200">
              <BaseIcon name="chat" class="w-6 h-6 mt-1 absolute" />
              <p class="pl-7 text-xs h-full truncate">
                Lorem, ipsum dolor sit amet consectetur adipisicing elit.
                Asperiores commodi excepturi aut quasi quo enim reprehenderit
                vero, aperiam quibusdam possimus nostrum, repellat corrupti
                laboriosam. Consectetur nisi eum eveniet quaerat. Mollitia!
              </p>
            </div>
          </div>
        </div>
      </div>
    </div> -->
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

  data(){
    return {
      questionQuery: '',
    }
  },

  methods: {
    askQuestion(){
      console.log(this.questionQuery)
      axios.post(`http://${process.env.VUE_APP_ASSISTANT_SEARCH_IP}/assistant/llamaSupportStream?text=${this.questionQuery}`,  {responseType: 'stream'},
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
