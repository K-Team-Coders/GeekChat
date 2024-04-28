<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-screen">
    <router-link to="/">
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
  </router-link>

    <div
      class="mx-24 w-full outline-dashed bg-frameBackground rounded-xl outline-[1px] outline-outlineColor duration-500">
      <!-- Блок процесса загрузки -->

      <div v-if="!isLoading" class="h-full  px-2 ">
        <div class="h-full relative flex justify-center">
          <!-- Блок ответов -->
          <div class="h-[85vh] overflow-y-auto p-16 w-full mb-16">


            <div :class="`${message.from[1]}`" v-for="message in spliceMessages">
              
              <div :class="`${message.from[0]}`">
                <p class="text-orange-300">{{message.username}}</p>
                <hr>
                <p :class="`${message.from[2]}`">{{message.message}}</p>
                <p class="text-gray-400 text-xs w-full text-end">{{dataFromatter(message.date)}}</p>
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
        <div class="rounded-full h-20 w-20  items-center justify-center flex text-red-600 uppercase font-stengazeta">
          Произошла ошибка!</div>
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

    spliceMessages() {
      let messages = this.messages;
      messages.forEach((message) => {
        if (message.username == this.myname) {
          message["from"] = this.isMessageFromMe("me")
        }
        else {
          message["from"] = this.isMessageFromMe("not_me")
        }
      })
      return messages
    }
  },

  data() {
    return {
      message: '',
      messages: [],
      sessionID: 1,
      isLoading: false,
      myname: '',
      isError: false,
      isReady: false,
      connection_data: null,
    };
  },

  methods: {
    sendMessage() {
      if (this.message.trim() !== "") {
        this.connection_data.send(this.message);
        console.log("Отправлено:")
        console.log(this.message)
        this.message = "";
      }
    },

    isMessageFromMe(name) {
      switch (name) {
        case "me":
          return ['max-w-96 bg-indigo-500 text-white rounded-lg p-3 gap-3', 'flex justify-end mb-4 cursor-pointer', 'text-gray-200 dark:text-gray-200']
        case "not_me":
          return ['max-w-96 dark:bg-white bg-slate-500 rounded-lg p-3 h-20 gap-3', 'flex mb-4 cursor-pointer', 'text-gray-700 dark:text-gray-700']
      }
    },

    dataFromatter(data) {
        let date = new Date(data);

        // Получаем день, месяц, год, часы, минуты и секунды
        let day = date.getDate();
        let month = date.getMonth() + 1; // Месяцы начинаются с 0, поэтому добавляем 1
        let year = date.getFullYear();
        let hours = date.getHours();
        let minutes = date.getMinutes();
        let seconds = date.getSeconds();

        // Форматируем день, месяц, часы, минуты и секунды, чтобы они были двузначными, если меньше 10
        day = day < 10 ? "0" + day : day;
        month = month < 10 ? "0" + month : month;
        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        // Создаем строку в формате "день.месяц.год часы:минуты:секунды"
        let formattedDate = hours + ":" + minutes + ":" + seconds + " " + day + "." + month + "." + year
        return formattedDate
    },
  },

  async mounted() {
    this.isLoading = true;
    await axios.get(`http://${process.env.VUE_APP_CHAT_SOCKET_IP}/register`)
      .then((response) => {
        console.log('Токен получен:');
        console.log(response.data);
        const name = response.data.token;
        this.myname = name;
      })

    console.log(this.myname);
    console.log("Подключение к веб-сокету...");
    let connection = new WebSocket(
      `ws://${process.env.VUE_APP_CHAT_SOCKET_IP}/ws/${this.sessionID}/${this.myname}`
    );

    connection.onopen = (event) => {
      console.log(event);
      console.log("Подключение успешно!");
      this.connection_data = connection;
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
      console.log("Получено:");
      console.log(JSON.parse(event.data));
      let parsed_message = JSON.parse(event.data)
      this.messages.push(parsed_message);
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
