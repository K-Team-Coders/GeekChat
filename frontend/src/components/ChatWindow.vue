<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-screen">
    <div class="flex-col">
      <div class="flex font-stengazeta uppercase text-activeText text-8xl">
        Пример чата
      </div>
      <div class="flex font-stengazeta uppercase text-activeText text-xl">
        *демонстративный
      </div>
      <div class="flex justify-start w-full bottom-8">
      <Switcher />
    </div>
    </div>
    <div
      class="mx-24 w-full outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <!-- Блок процесса загрузки -->

      <div v-if="!isLoading" class="h-full  px-2 ">
        <div class="h-full relative flex justify-center">
          <!-- Блок ответов -->
          <div class="h-[85vh] overflow-y-auto p-16 w-full mb-16">

            <!-- Входящее сообщение -->
            <div class="flex mb-4 cursor-pointer">
              <div class="w-9 h-9 rounded-full flex items-center justify-center ml-2">
                <img src="https://placehold.co/200x/b7a8ff/ffffff.svg?text=Я&font=Lato" alt="My Avatar"
                  class="w-8 h-8 rounded-full" />
              </div>
              <div class="max-w-96 dark:bg-white bg-slate-200 rounded-lg p-3 gap-3">
                <p class="text-gray-700">игорь хуесос?</p>
                <p class="text-gray-400 text-xs w-full text-end">20:00</p>
              </div>
            </div>

            <!-- Исходящее сообщение -->
            <div class="flex justify-end mb-4 cursor-pointer">
              <div class="max-w-96 bg-indigo-500 text-white rounded-lg p-3 gap-3">
                <p class="text-white">кисель хуесос?</p>
                <p class="text-gray-200 text-xs w-full text-end">20:00</p>
              </div>
              <div class="w-9 h-9 rounded-full flex items-center justify-center ml-2">
                <img src="https://placehold.co/200x/b7a8ff/ffffff.svg?text=Я&font=Lato" alt="My Avatar"
                  class="w-8 h-8 rounded-full" />
              </div>
            </div>
          </div>
          <div class="absolute bottom-3 w-full flex items-center gap-2 justify-center px-2">
            <input v-model="message"
              class="w-11/12 rounded-xl h-10 border-[1.5px] bg-transparent px-4 text-activeText placeholder:text-unactiveText border-neutral-500 dark:border-neutral-200 duration-500"
              type="text" placeholder="Спрашивайте все, что угодно..." />

            <button @click="sendMessage()" class="">
              <svg :style="{ fill: isDarkMode ? 'white' : 'black' }" class="w-7 h-7 cursor-pointer" viewBox="0 0 24 24"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M4.10514201,11.8070619 L2.74013818,2.2520351 L22.236068,12 L2.74013818,21.7479649 L4.10514201,12.1929381 L4.87689437,12 L4.10514201,11.8070619 Z M5.25986182,5.7479649 L5.89485799,10.1929381 L13.1231056,12 L5.89485799,13.8070619 L5.25986182,18.2520351 L17.763932,12 L5.25986182,5.7479649 Z" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      <div v-if="isLoading" class="flex justify-center items-center h-screen">
        <div class="rounded-full h-20 w-20 bg-violet-800 items-center justify-center flex animate-ping"></div>
      </div>

      <div v-else-if="isError" class="flex justify-center items-center h-screen">
        <div class="rounded-full h-20 w-20  items-center justify-center flex text-red-600 uppercase font-stengazeta">Произошла ошибка!</div>
      </div>
    </div>
    
  </div>
</template>
<script>
import axios from "axios";
import BaseIcon from "./BaseIcon.vue";
import Switcher from "./Switcher.vue";
export default {
  components: {
    BaseIcon,
    Switcher,
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },

  data() {
    return {
      message: '',
      messages: [],
      sessionID: 1,
      isLoading: false,
      isError: false,
      isReady: false,
    };
  },

  methods: {
    sendMessage() {
      if (this.message.trim() !== "") {
        this.connection.send(String({ type: "communication", message: this.message }));
        this.message = "";
      }
    },
  },

  mounted() {
    this.isLoading = true;
    console.log("Подключение к веб-сокету...");
    let connection = new WebSocket(
      `ws://${process.env.VUE_APP_CHAT_SOCKET_IP}/ws/session_id=${this.sessionID}`
    );

    connection.onopen = (event) => {
      console.log(event);
      console.log("Подключение успешно!");
      this.connection.send(String({ type: "service", message: "WAI?" }));
      this.isLoading = false;
    };

    connection.onclose = (event) => {
      if (event.wasClean) {
        console.log(
          `[close] Соединение закрыто чисто, код=${event.code} причина=${event.reason}`
        );
        this.isLoading = false;
      } else {
        // например, сервер убил процесс или сеть недоступна
        // обычно в этом случае event.code 1006
        console.log("[close] Соединение прервано");
        this.isLoading = false;
      }
    };

    connection.onerror = (error) => {
      console.log(`[error]`);
      this.isLoading = false;
    };

    connection.onmessage = (event) => {
      this.messages.push(event.data);
    };
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
