<template>
  <div class="min-h-screen w-full bg-background duration-500">
    <div class="">
      <Overlay />
    </div>
    <div>
      <Header />
    </div>
    <div class="fixed right-2 -top-3">
      <Switcher />
    </div>
    <div class="">
      <HeaderTimeAndDate />
    </div>
    <div class="flex justify-center">
      <div class="w-8/12">
        <div class="pt-16 relative">
          <form class="" @submit.prevent="">
            <input
              class="w-full rounded-lg focus:rounded-t-lg h-10 bg-slate-50 px-4 py-[20px] shadow-4xl disabled:bg-slate-300 text-activeText dark:text-black active:outline-none placeholder:text-neutral-500 duration-500 focus:outline-none"
              type="text"
              :placeholder="
                isError
                  ? 'Произола ошибка. Проверьте соединение'
                  : isLoading
                  ? 'Загрузка...Пожалуйста, подождите'
                  : 'Введите запрос'
              "
              v-model="query"
              @input="handleInput"
              :disabled="isError || isLoading"
            />
          </form>
          <ul
            v-if="query.length"
            class="absolute top-[98px] w-full py-2 z-50 border-t-[1px] border-gray-200 rounded-b-lg dark:text-black bg-slate-50 shadow-5xl text-activeText"
          >
            <li
              class="hover:bg-neutral-300 bg-neutral-200 duration-300 py-0.5 cursor-pointer"
            >
              <router-link :to="{ path: '/search_document', query: { text: makeDocQuerry }}">
                <div class="flex justify-between">
                  <span class="px-4 font-semibold py-2">
                    {{ query }}
                  </span>
                  <span class="px-4 font-semibold py-2 text-gray-900">
                    Поиск в документах
                  </span>
                </div>
              </router-link>
            </li>
            <li
              v-for="(item, index) in makeHelpList.slice(0, 3)"
              class="hover:bg-neutral-200 duration-300 py-0.5 cursor-pointer"
              :key="index"
            >
              <router-link :to="item.url">
                <div class="flex justify-between">
                  <span class="px-4 font-semibold py-2">
                    {{ item.name }}
                  </span>
                  <span
                    class="px-4 font-semibold py-2"
                    :class="`text-${chooseColor(
                      item.probability.toFixed(2)
                    )}-900`"
                  >
                    {{ item.probability.toFixed(2) }}
                  </span>
                </div>
              </router-link>
            </li>
          </ul>
        </div>
        <div class="flex flex-col pt-52 gap-4 mb-3" v-if="query.length > 0">
          <div
            class="rounded-lg min-h-10 shadow-4xl text-activeText bg-neutral-100 dark:bg-neutral-100 dark:text-black p-3"
          >
            <p class="text-xs font-bold">Быстрый ответ ассистента:</p>
            <SmallLoader class="pt-2.5" v-if="isWaitingLama" />
            <p v-else>{{ llamaMessage }}</p>
          </div>
          <div
            class="rounded-lg min-h-10 shadow-4xl text-activeText bg-neutral-100 dark:bg-neutral-100 dark:text-black p-3"
          >
            <p class="text-xs font-bold">Быстрый ответ из википедии:</p>
            <SmallLoader class="pt-2.5" v-if="isWaitingWiki" />
            <p v-else>
              {{ wikiMessage }}
            </p>
          </div>
        </div>
        <div class="grid grid-cols-4 gap-2.5 pt-4" v-if="query == ''">
          <Card
            v-for="card in datacard"
            :key="card"
            :title="card.name"
            :subtitle="card.subtitle"
            :url="card.url"
            :name="card.icon"
          />
        </div>
      </div>
      <transition
        enter-active-class="transition ease-in-out duration-500 transform"
        enter-from-class="translate-x-full"
        enter-to-class="translate-x-0"
        leave-active-class="transition ease-in-out duration-500 transform"
        leave-from-class="translate-x-0"
        leave-to-class="translate-x-full"
      >
        <Alert v-if="isError" @close="isError = false" />
        <AlertIsLoading v-else-if="isLoading" @close="isLoading = false" />
        <AlertisReady v-else-if="isReady" @close="isReady = false" />
      </transition>
    </div>
  </div>
</template>

<script>
import Sova from "@/components/Sova.vue";
import Header from "@/components/Header.vue";
import Card from "@/components/Card.vue";
import BaseIcon from "@/components/BaseIcon.vue";
import Switcher from "@/components/Switcher.vue";
import HeaderTimeAndDate from "@/components/HeaderTimeAndDate.vue";
import Overlay from "@/components/Overlay.vue";
import Alert from "@/components/Alert.vue";
import AlertIsLoading from "../components/AlertIsLoading.vue";
import AlertisReady from "../components/AlertisReady.vue";
import SmallLoader from "@/components/SmallLoader.vue";
import TranslaterLoader from "@/components/TranslaterLoader.vue";
export default {
  components: {
    Sova,
    Card,
    Header,
    BaseIcon,
    Switcher,
    HeaderTimeAndDate,
    Alert,
    Header,
    Overlay,
    AlertIsLoading,
    AlertisReady,
    SmallLoader,
    TranslaterLoader,
  },

  data() {
    return {
      datacard: [
        {
          name: "Ассистент",
          subtitle: "Информационный справочник",
          url: "/assistant",
          icon: "chat",
        },
        {
          name: "Поиск документов",
          subtitle:
            "Возможность найти определенный документ из общей базы данных документов",
          url: "/search_document/",
          icon: "search",
        },
        {
          name: "Переводчик",
          subtitle:
            "Возможность перевода с иностранных языков на русский и наоборот",
          url: "/translater",
          icon: "translate",
        },
        {
          name: "Распознавание текста",
          subtitle: "Возможность распознать текст с картинки",
          url: "/scan_from_docs",
          icon: "eye",
        },

        {
          name: "Распознавание аудио",
          subtitle: "Преобразование голосовой речи в текстовый формат",
          url: "/audio_recognition",
          icon: "microphone",
        },
        {
          name: "Преобразование текста в аудио",
          subtitle: "Преобразование текста в аудио",
          url: "/text_to_audio",
          icon: "gromko",
        },
        {
          name: "Распознавание на изображении",
          subtitle: "Возможность узнать что за объект на фотографии",
          url: "/image_recognition",
          icon: "flag",
        },
        {
          name: "Формирование документов",
          subtitle: "хз",
          url: "/",
          icon: "news",
        },
      ],
      query: '',
      filteredData: [],
      llamaMessage: "",
      wikiMessage: "",
      isError: false,
      isLoading: true,
      typingTimeout: null,
      isReady: false,
      isWaitingLama: false,
      isWaitingWiki: false,
    };
  },

  computed: {
    makeHelpList() {
      return this.filteredData;
    },

    makeDocQuerry(){
      return this.query == null ? '' : this.query
    }
  },

  methods: {
    chooseColor(prob) {
      let color;
      if (0 <= prob < 0.33) {
        color = "red";
      } else if (0.33 <= prob < 0.66) {
        color = "orange";
      } else if (0.66 <= prob < 1) {
        color = "green";
      }
      console.log(color);
      return color;
    },

    sendQuerry() {
      const inputText = this.query;
      if (inputText.trim()) {
        this.assistantLamma.send(inputText);
        this.assistantWiki.send(inputText);
      }
      this.typingTimeout = null;
    },

    handleInput(event) {
      const inputText = event.target.value;
      if (inputText.trim()) {
        this.connection.send(inputText);
      }
      this.isWaitingLama = true;
      this.isWaitingWiki = true;
      clearTimeout(this.typingTimeout);
      this.typingTimeout = setTimeout(() => {
        this.sendQuerry();
      }, 5000);
    },

    receiveServices(event) {
      this.filteredData = JSON.parse(event.data);
    },
  },

  mounted() {
    this.connection = new WebSocket(
      `ws://${process.env.VUE_APP_SERVICE_SEARCH_IP}/searchHelper`
    );
    this.assistantLamma = new WebSocket(
      `ws://${process.env.VUE_APP_ASSISTANT_SEARCH_IP}/assistant/llamaSupport`
    );
    this.assistantWiki = new WebSocket(
      `ws://${process.env.VUE_APP_ASSISTANT_SEARCH_IP}/assistant/wikiSupport`
    );
    setTimeout(() => {
      this.isError = false;
      this.isReady = false;
    }, 4000);

    this.connection.onopen = () => {
      console.log("Соединение подсказок установлено!");
      this.isLoading = false;
      this.isReady = true;
    };
    this.assistantLamma.onopen = () => {
      console.log("Соединение лама установлено!");
    };
    this.assistantWiki.onopen = () => {
      console.log("Соединение вики установлено!");
    };

    this.connection.onmessage = this.receiveServices;

    this.assistantLamma.onmessage = (event) => {
      if (typeof event.data === "string") {
        this.llamaMessage = event.data;
        this.isWaitingLama = false;
      } else {
        console.error("Received non-text data from the server:", event.data);
      }
    };
    this.assistantWiki.onmessage = (event) => {
      if (typeof event.data === "string") {
        this.wikiMessage = event.data;
        this.isWaitingWiki = false;
        console.log(this.assistantWiki);
      } else {
        console.error("Received non-text data from the server:", event.data);
      }
    };

    this.connection.onclose = (event) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };

    this.connection.onerror = (error) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };
    this.assistantLamma.onclose = (event) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };

    this.assistantLamma.onerror = (error) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };

    this.assistantWiki.onclose = (event) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };

    this.assistantWiki.onerror = (error) => {
      console.log(this);
      this.isError = true;
      this.isLoading = false;
    };
  },
};
</script>

<style></style>
