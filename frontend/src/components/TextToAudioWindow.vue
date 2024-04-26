<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col min-h-[92vh] duration-500 justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <LoaderBig v-if="isLoading" />
      <div v-else-if="isError" class="flex justify-center pl-20">
        <ErrorPage :status="error_info.code" :text="error_info.message" />
      </div>
      <div v-else class="w-10/12 mb-10">
        <div class="flex justify-center mb-4 pt-10">
          <p
            class="text-center text-4xl font-black font-mono text-activeText duration-500"
          >
            Преобразование текста в аудио
          </p>
        </div>
        <div
          class="text-activeText text-xl rounded uppercase text-center duration-500"
        >
          <div class="flex flex-row gap-3">
            <select
              class="hover:bg-hoverBackground bg-outputBackground text-xl focus:outline-none focus:ring-0 focus:border-none uppercase rounded-t-xl text-center py-2 duration-500 w-full h-full"
              v-model="choosed_speaker"
              style=""
            >
              Выберите голос
              <option
                value=""
                disabled
                selected
                class="text-activeText duration-500"
              >
                Выберите голос озвучки
              </option>
              <option
                class="normal-case"
                v-for="(speaker, index) in this.speakers"
                :key="index"
              >
                {{ speaker + 1 }}
              </option>
            </select>
            <select
              class="hover:bg-hoverBackground bg-outputBackground text-xl focus:outline-none focus:ring-0 focus:border-none uppercase rounded-t-xl text-center py-2 duration-500 w-full h-full"
              v-model="choosed_language"
              style=""
            >
              Выберите язык
              <option
                value=""
                disabled
                selected
                class="text-activeText duration-500"
              >
                Выберите язык озвучки
              </option>
              <option
                class="normal-case"
                v-for="(language, index) in this.languages"
                :key="index"
              >
                {{ language.name }}
              </option>
            </select>
          </div>
        </div>
        <div
          class="w-full h-12 border-2 border-outputBorder flex gap-8 items-center justify-center duration-500"
        >
          <button
            @click="addEmotes(emote)"
            class="text-contrast dark:text-neutral-200 duration-500 shadow-md px-3 py-1 rounded-md"
            v-for="emote in emotes"
            :class="`bg-[${emote.color}]`"
            :key="emote"
          >
            {{ emote.name }}
          </button>
        </div>
        <div>
          <form class="flex flex-col gap-2">
            <textarea
              v-model="origin_text"
              type="text"
              placeholder="Напишите сообщение для озвучки"
              class="max-h-[800px] shadow-md min-h-[450px] w-full custom-scrollbar bg-outputBackground text-activeText pl-6 pt-4 pb-4 pr-14 h-[335px] text-wrap rounded-bl-xl focus:outline-none focus:ring-0 text-xl focus:border-none text-start placeholder:text-unactiveText duration-500"
              onkeyup="this.style.height = 'auto'; this.style.height = this.scrollHeight + 'px'"
            />
            <button
              @click.prevent="submitText()"
              type="submit"
              class="text-activeText shadow-md bg-buttonBackground hover:bg-buttonHover duration-500 focus:ring-4 focus:outline-none focus:ring-buttonBackground font-semibold rounded-xl text-sm w-full sm:w-auto px-5 py-2.5 text-center"
            >
              Отправить текст на озвучку
            </button>
          </form>
        </div>
        <div class="flex justify-center">
          <TranslaterLoader v-if="isLoading" />
        </div>
        <figure class="text-activeText pt-2 w-full" v-if="audioIsReady">
          <figcaption class="text-xl">Прослушать аудио</figcaption>
          <audio controls :src="target_audio_path" class="w-full pt-2"></audio>
        </figure>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TranslaterLoader from "./TranslaterLoader.vue";
import SidebarMain from "./SidebarMain.vue";
import LoaderBig from "./LoaderBig.vue";
import ErrorPage from "./ErrorPage.vue";
export default {
  components: {
    TranslaterLoader,
    SidebarMain,
    LoaderBig,
    ErrorPage,
  },
  data() {
    return {
      origin_text: "",
      sent_message: "",
      last_emote: "",
      target_audio_path: "",
      target_language: "",
      choosed_speaker: "1",
      choosed_language: "Русский",
      isLoading: false,
      audioIsReady: false,
      isProcessing: false,
      speakers: [0, 1, 2, 3, 4, 5, 6, 7, 8],
      languages: [],
      isError: false,
      error_info: false,
      emotes: [
        {
          name: "[СМЕХ]",
          code: "[laughter]",
          color: "green",
        },
        {
          name: "[СМЕШОК]",
          code: "[laughs]",
          color: "#6b1f66",
        },
        {
          name: "[ВЗДОХ]",
          code: "[sighs]",
          color: "blue",
        },
        {
          name: "[МУЗЫКА]",
          code: "[music]",
          color: "#8c7a12",
        },
        {
          name: "[ЗАПЫХАЕТСЯ]",
          code: "[gasps]",
          color: "black",
        },
        {
          name: "[КАШЛЯЕТ]",
          code: "[clears throat]",
          color: "red",
        },
      ],
    };
  },
  methods: {
    submitText() {
      (this.isLoading = true),
        axios
          .post(
            `http://${process.env.VUE_APP_TEXT_TO_AUDIO_SERVICE_IP}/textToSpeech/processText/`,
            {
              message: this.origin_text,
              speaker: String(this.choosed_speaker - 1),
              target_language: this.choose_target_language_iso,
            }
          )
          .then((response) => {
            console.log("Название файла");
            console.log(response.data.filename);
            this.target_audio_path = `http://${process.env.VUE_APP_TEXT_TO_AUDIO_SERVICE_IP}/textToSpeech/processedText/${response.data.filename}`;
            this.isLoading = false;
            this.audioIsReady = true;
          })
          .catch(function () {
            console.log("Ошибка в обработке");
            this.isLoading = false;
            this.isError = true;
          });
    },
    addEmotes(emote) {
      this.origin_text += " " + emote.code + " ";
      this.last_emote = emote.name;
    },
  },

  computed: {
    choose_target_language_iso() {
      return this.languages.find(
        (language) => language.name == this.choosed_language
      ).iso;
    },
    make_message() {
      return this.emotes.find((emote) => this.last_emote == emote.name).code;
    },
  },
  created() {
    this.isLoading = true;
    axios
      .get(
        `http://${process.env.VUE_APP_TEXT_TO_AUDIO_SERVICE_IP}/textToSpeech/getAvailiableLanguages`
      )
      .then((response) => {
        console.log("Загруженные языки для озучки текста");
        this.languages = response.data.result;
      
        console.log(this.languages);
        this.isLoading = false;
      })
      .catch((response) => {
        this.isLoading = false;
        this.isError = true;
        console.log(response);
        this.error_info = response;
      });
  },
};
</script>

<style></style>
