<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6 z-50">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col min-h-[90vh] duration-500 justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <LoaderBig v-if="isLoading" class=""/>
      
      <div v-else-if="isError" class="flex justify-center">
        <ErrorPage :status="error_info.code" :text="error_info.message" />
      </div>
      <div v-else class="w-full mx-24 flex flex-col justify-center mb-10">
        <div class="flex justify-center mb-4 pt-10">
          <p
            class="text-center text-4xl font-black font-mono text-activeText duration-500"
          >
            Переводчик
          </p>
        </div>
        <div
          class="flex flex-col mx-24 font-medium shadow-xl rounded-xl justify-center"
        >
          <div
            class="flex justify-around bg-buttonBackground duration-500 rounded-t-xl items-center border-b-2 border-buttonHover"
          >
            <div class="w-full">
              <div
                class="text-activeText text-xl uppercase hover:bg-buttonHover hover:rounded-tl-xl text-center rounded-tl-xl duration-500"
              >
                <select
                  class="bg-buttonBackground hover:bg-buttonHover text-xl focus:outline-none focus:ring-0 focus:border-none uppercase rounded-tl-xl hover:rounded-tl-xl text-center py-2 duration-500 w-full h-full"
                  v-model="origin_language"
                  style="appearance: none"
                >
                  Выберите язык
                  <option
                    class="normal-case"
                    v-for="(language, index) in origin_languages"
                    :key="index"
                  >
                    {{ language.name }}
                  </option>
                </select>
              </div>
            </div>
            <div
              @click="swap_language()"
              class="text-activeText text-xl uppercase py-2 mx-2 rounded-full hover:bg-buttonHover duration-500"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-10 h-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M7.5 21 3 16.5m0 0L7.5 12M3 16.5h13.5m0-13.5L21 7.5m0 0L16.5 12M21 7.5H7.5"
                />
              </svg>
            </div>
            <div class="w-full text-center">
              <div
                class="text-activeText text-xl uppercase hover:bg-buttonHover hover:rounded-tr-xl text-center rounded-tr-xl duration-500"
              >
                <select
                  style="appearance: none"
                  class="bg-buttonBackground hover:bg-buttonHover duration-500 text-xl focus:outline-none focus:ring-0 focus:border-none uppercase rounded-tr-xl hover:rounded-tl-xl text-center py-2 w-full h-full"
                  v-model="target_language"
                >
                  <option
                    class="normal-case"
                    v-for="language in make_target_languages"
                    :key="language"
                  >
                    {{ language.name }}
                  </option>
                </select>
              </div>
            </div>
          </div>
          <div class="h-96 flex duration-500">
            <div
              class="w-1/2 bg-buttonBackground duration-500 rounded-bl-xl border-buttonHover"
            >
              <div class="relative">
                <form class="absolute w-full duration-500" action="">
                  <textarea
                    @input="text_processing()"
                    ref="myinput"
                    v-model="origin_message"
                    v-on:focus="$event.target.select()"
                    class="w-full custom-scrollbar duration-500 bg-buttonBackground text-activeText pl-6 pt-4 pb-4 pr-14 h-[335px] text-wrap rounded-bl-xl focus:outline-none focus:ring-0 text-xl focus:border-none text-start placeholder:text-unactiveText"
                    type="text"
                    style="resize: none"
                    placeholder="Начните писать или вставьте текст"
                  ></textarea>
                  <div class="relative h-full">
                    <div
                      class="absolute rounded-xl -top-2 left-2 flex justify-center items-center p-2.5 hover:bg-buttonHover duration-500 cursor-pointer"
                    >
                      <svg
                        @click="copy_origin_text"
                        class="w-6 h-6"
                        version="1.1"
                        id="Capa_1"
                        xmlns="http://www.w3.org/2000/svg"
                        xmlns:xlink="http://www.w3.org/1999/xlink"
                        viewBox="0 0 210.107 210.107"
                        xml:space="preserve"
                      >
                        <g>
                          <path
                            :style="{ fill: isDarkMode ? 'white' : 'black' }"
                            d="M168.506,0H80.235C67.413,0,56.981,10.432,56.981,23.254v2.854h-15.38
		c-12.822,0-23.254,10.432-23.254,23.254v137.492c0,12.822,10.432,23.254,23.254,23.254h88.271
		c12.822,0,23.253-10.432,23.253-23.254V184h15.38c12.822,0,23.254-10.432,23.254-23.254V23.254C191.76,10.432,181.328,0,168.506,0z
		 M138.126,186.854c0,4.551-3.703,8.254-8.253,8.254H41.601c-4.551,0-8.254-3.703-8.254-8.254V49.361
		c0-4.551,3.703-8.254,8.254-8.254h88.271c4.551,0,8.253,3.703,8.253,8.254V186.854z M176.76,160.746
		c0,4.551-3.703,8.254-8.254,8.254h-15.38V49.361c0-12.822-10.432-23.254-23.253-23.254H71.981v-2.854
		c0-4.551,3.703-8.254,8.254-8.254h88.271c4.551,0,8.254,3.703,8.254,8.254V160.746z"
                          />
                        </g>
                      </svg>
                    </div>
                  </div>
                </form>
                <BaseIcon
                  @click="delete_text"
                  name="x"
                  class="w-6 h-6 duration-500 text-activeText absolute right-3 top-3 cursor-pointer rounded-xl hover:text-red-900"
                />
              </div>
            </div>
            <div class="w-1/2 bg-buttonHover duration-500 rounded-br-xl">
              <div class="relative">
                <svg
                  @click="copy_target_text"
                  class="w-10 h-10 text-activeText absolute right-3 top-3 cursor-pointer rounded-xl hover:bg-buttonBackground p-2"
                  version="1.1"
                  id="Capa_1"
                  xmlns="http://www.w3.org/2000/svg"
                  xmlns:xlink="http://www.w3.org/1999/xlink"
                  viewBox="0 0 210.107 210.107"
                  xml:space="preserve"
                >
                  <g>
                    <path
                      :style="{ fill: isDarkMode ? 'white' : 'black' }"
                      d="M168.506,0H80.235C67.413,0,56.981,10.432,56.981,23.254v2.854h-15.38
		c-12.822,0-23.254,10.432-23.254,23.254v137.492c0,12.822,10.432,23.254,23.254,23.254h88.271
		c12.822,0,23.253-10.432,23.253-23.254V184h15.38c12.822,0,23.254-10.432,23.254-23.254V23.254C191.76,10.432,181.328,0,168.506,0z
		 M138.126,186.854c0,4.551-3.703,8.254-8.253,8.254H41.601c-4.551,0-8.254-3.703-8.254-8.254V49.361
		c0-4.551,3.703-8.254,8.254-8.254h88.271c4.551,0,8.253,3.703,8.253,8.254V186.854z M176.76,160.746
		c0,4.551-3.703,8.254-8.254,8.254h-15.38V49.361c0-12.822-10.432-23.254-23.253-23.254H71.981v-2.854
		c0-4.551,3.703-8.254,8.254-8.254h88.271c4.551,0,8.254,3.703,8.254,8.254V160.746z"
                    />
                  </g>
                </svg>
                <output
                  class="w-full h-48 rounded-br-xl text-activeText p-4 duration-500"
                  v-on:focus="$event.target.select()"
                  ref="myoutput"
                >
                  {{ target_message.result }}</output
                >
              </div>
            </div>
          </div>
        </div>
        <div class="flex justify-center mx-24">
          <div
            class="w-full h-48 text-activeText pt-4 duration-500 flex flex-col justify-center"
          >
            <FormsFile :url="1" :textisProcessing="textisProcessing" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import SmallLoader from "./SmallLoader.vue";
import FormsFile from "./FormsFile.vue";
import debounce from "lodash/debounce";
import BaseIcon from "./BaseIcon.vue";
import ErrorPage from "@/components/ErrorPage.vue";
import SidebarMain from "@/components/SidebarMain.vue";
import LoaderBig from "./LoaderBig.vue";

export default {
  components: {
    BaseIcon,
    SmallLoader,
    FormsFile,
    ErrorPage,
    SidebarMain,
    LoaderBig,
  },
  data() {
    return {
      origin_language: "Русский",
      target_language: "Английский",
      origin_message: "",
      target_message: "",
      isLoading: false,
      isError: false,
      isTyping: false,
      textisProcessing: false,
      error_info: "",
      origin_languages: [],
    };
  },
  methods: {
    swap_language() {
      this.origin_language = [
        this.target_language,
        (this.target_language = this.origin_language),
      ][0];
      this.origin_message = [
        this.target_message,
        (this.target_message = this.origin_message),
      ][0];
    },
    delete_text() {
      this.origin_message = "";
      this.target_message = "";
    },
    copy_origin_text() {
      this.$refs.myinput.focus();
      document.execCommand("copy");
    },
    copy_target_text() {
      this.$refs.myoutput.focus();
      document.execCommand("copy");
    },

    debounceStopTyping: debounce(function () {
      this.isTyping = false;
    }, 500),

    text_processing() {
      this.isError = false;
      this.isTyping = true;
      this.textisProcessing = true;
      this.debounceStopTyping();
      setTimeout(() => {
        if (this.isTyping == false) {
          axios
            .post(
              `http://${process.env.VUE_APP_TRANSLATE_SERVICE_IP}/translator/translateText/`,
              {
                origin: this.choose_origin_iso639_1,
                target: this.choose_source_iso639_1,
                message: this.origin_message,
              }
            )
            .then((response) => {
              this.target_message = response.data;
              this.textisProcessing = false;
            })
            .catch(function () {
              console.log("Ошибка в обработке");
              this.textisProcessing = false;
              this.isError = true;
            });
        }
      }, 500);
    },
  },
  computed: {
    make_target_languages() {
      try {
        let target_values = this.origin_languages.find(
          (language) => language.name == this.origin_language
        );
        console.log(target_values);
        return target_values.targets;
      } catch (err) {
        console.log(err);
      }
    },
    choose_origin_iso639_1() {
      return this.origin_languages.find(
        (language) => language.name == this.origin_language
      ).iso;
    },
    choose_source_iso639_1() {
      return this.make_target_languages.find(
        (language) => language.name == this.target_language
      ).iso;
    },
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  created() {
    this.isLoading = true;
    axios
      .get(
        `http://${process.env.VUE_APP_TRANSLATE_SERVICE_IP}/translator/modelGarden`
      )
      .then((response) => {
        this.origin_languages = response.data.languages;
        console.log(this.origin_languages);
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

<style scoped>
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
