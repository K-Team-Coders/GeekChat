<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 ">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="flex duration-500 flex-col min-h-[93vh] pt-14 ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <div class="flex mb-4">
        <p
          class="text-center text-4xl font-black font-mono text-activeText duration-500"
        >
          Сканировать текст с фотографии
        </p>
      </div>
      <div :class="classes">
        <form>
          <div class="flex justify-start items-center">
            <button
              @click="$refs.files.click()"
              :style="{ fill: isDarkMode ? 'white' : 'black' }"
            >
              <svg
                version="1.1"
                id="Capa_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                class="w-6 h-6 mr-2"
                viewBox="0 0 30.58 30.58"
                xml:space="preserve"
              >
                <g>
                  <path
                    style="dark:fill: #ffffff fill:#000000"
                    d="M28.692,3.179c-1.892-1.892-4.867-3.428-8.295,0L6.5,17.075c-0.107,0.096-1.386,1.297-1.431,3.039 c-0.028,1.076,0.413,2.079,1.313,2.979c0.768,0.768,1.687,1.167,2.655,1.155c1.754-0.021,3.062-1.343,3.204-1.493l10.455-10.454 c0.391-0.391,0.392-1.023,0-1.414c-0.391-0.391-1.023-0.391-1.414,0L10.811,21.358c-0.249,0.256-1.029,0.884-1.807,0.89 c-0.426,0.003-0.821-0.184-1.208-0.57c-0.5-0.5-0.738-0.99-0.728-1.501c0.017-0.907,0.805-1.647,0.813-1.656l13.93-13.928 c1.352-1.351,3.059-2.409,5.467,0c0.882,0.882,1.319,1.796,1.302,2.718c-0.029,1.515-1.257,2.667-1.27,2.679L11.691,25.434 c-0.034,0.034-1.965,1.986-4.316,2.002c-1.237,0.008-2.412-0.536-3.492-1.615c-4.082-4.082-0.262-8.156-0.098-8.327L15.798,5.48 c0.391-0.391,0.391-1.023,0-1.415c-0.392-0.391-1.024-0.39-1.414,0L2.356,16.093c-1.878,1.956-4.249,6.78,0.112,11.142 c1.478,1.477,3.139,2.217,4.937,2.2c3.198-0.028,5.608-2.491,5.709-2.596l15.574-15.4c0.044-0.039,1.832-1.686,1.891-4.064 C30.616,5.879,29.981,4.467,28.692,3.179z"
                  />
                </g>
              </svg>
            </button>
            <input
              class="w-full text-sm text-inputText shadow-md border-[0.5px] py-1 px-2 border-inputBorder rounded-lg cursor-pointer bg-inputBackground focus:outline-none"
              aria-describedby="file_input_help"
              id="files"
              ref="files"
              type="file"
              accept="image/png, image/jpeg, application/pdf"
              @change="handleFilesUpload()"
            />
            <p
              class="w-[6%] mt-2.5 ml-2 text-sm text-activeText text-end duration-500"
              id="file_input_help"
            >
              .jpeg .jpg
            </p>
          </div>

          <div class="py-4">
            <div class="text-activeText">
              <div class="">
                <div class="flex items-center justify-between w-full gap-2">
                  <p class="text-activeText duration-500">
                    Выберите язык, который используется на фотографии:
                  </p>
                  <div
                    class="text-activeText duration-500 shadow-md text-xl rounded-xl uppercase hover:bg-buttonHover hover:rounded-tl-xl text-center rounded-tl-xl"
                  >
                    <select
                      class="bg-buttonBackground duration-500 hover:bg-buttonHover text-activeText text-xl focus:outline-none rounded-xl focus:ring-0 focus:border-none uppercase text-center py-2 w-96 h-full"
                      v-model="language"
                      style=""
                    >
                      Выберите язык
                      <option
                        class="normal-case rounded-xl"
                        v-for="(language, index) in origin_languages"
                        :key="index"
                      >
                        {{ language }}
                      </option>
                    </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
      <div class="pt-4 w-10/12">
        <transition
          enter-active-class="transition-opacity easy-linear duration-500"
          enter-from-class="opacity-0"
          enter-to-class="opacity-100"
          leave-active-class="transition-opacity easy-linear duration-500"
          leave-from-class="opacity-100"
          leave-to-class="opacity-0"
        >
          <div class="flex flex-col gap-2 items-center">
            <div
              class="flex min-w-[200px] min-h-[323px] max-h-[800px] rounded-xl border-2 border-outputBorder bg-outputBackground p-4 duration-500"
              v-for="file in files"
              :key="file"
            >
              <img v-if="isPhoto" :src="url" />
            </div>
            <div class="w-full pt-2">
              <div class="flex justify-center">
                <TranslaterLoader v-if="isLoading" />
                <transition
                  enter-active-class="transition ease-in-out duration-500 transform"
                  enter-from-class="translate-x-full"
                  enter-to-class="translate-x-0"
                  leave-active-class="transition ease-in-out duration-500 transform"
                  leave-from-class="translate-x-0"
                  leave-to-class="translate-x-full"
                >
                  <Alert v-if="isError" @close="isError = false" />
                </transition>
              </div>
              <div class="">
                <TextOutput
                  v-if="isReady"
                  :text="text_massage"
                  :language="text_language"
                />
              </div>
            </div>
          </div>
        </transition>
        <div class="flex justify-end pt-2">
          <div class="mb-8">
            <button
              @click.prevent="scrollToBottom"
              type="submit"
              class="text-activeText h-11 shadow-md bg-buttonBackground hover:bg-buttonHover duration-500 focus:ring-4 focus:outline-none focus:ring-buttonBackground font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center"
            >
              Отправить файл
            </button>
          </div>
        </div>
        <!-- <iframe
          src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210101201653/PDF.pdf"
          width="800"
          height="700"
        >
        </iframe> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TextOutput from "./TextOutput.vue";
import TranslaterLoader from "./TranslaterLoader.vue";
import SidebarMain from "./SidebarMain.vue";
import Alert from "./Alert.vue";
export default {
  components: {
    TextOutput,
    TranslaterLoader,
    SidebarMain,
    Alert,
  },
  data() {
    return {
      isPhoto: false,
      uploadFile: "",
      files: [],
      url: "",
      isError: false,
      isOpen: false,
      text_language: "",
      text_massage: "",
      isLoading: false,
      isReady: false,
      target_languages: [],
      origin_languages: ["английский", "арабский", "русский", "украинский"],
    };
  },
  computed: {
    classes() {
      return this.isPhoto ? "w-10/12" : ["w-10/12", "pt-8"];
    },
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  methods: {
    handleFilesUpload() {
      this.uploadFile = this.$refs.files.files[0];
      const typeFile = this.uploadFile.type;
      this.url = URL.createObjectURL(this.uploadFile);
      console.log(typeFile);
      this.files.push(this.uploadFile.name);
      console.log(this.files);
      if (
        this.uploadFile.type.startsWith("image") ||
        this.uploadFile.type.startsWith("application")
      ) {
        this.isPhoto = true;
      } else {
        this.isPhoto = false;
      }
    },
    scrollToBottom() {
      window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth",
      });
      this.submitFiles();
    },
    async submitFiles() {
      this.isLoading = true;
      const formData = new FormData();
      formData.append("file", this.uploadFile);
      const language = this.language;
      console.log(language);
      console.log(formData);
      axios
        .post(
          `http://${process.env.VUE_APP_OCR_SERVICE_IP}/ocr_pdf_image`,
          formData,
          {
            params: {
              language,
            },
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          this.text_massage = response.data.text;
          this.text_language = response.data.language;
          this.isLoading = false;
          this.isReady = true;
          console.log(this.text_massage);
          console.log(this.text_language);
        })
        .catch(
          function (error) {
            console.log("Ошибка в обработке:", error);
            this.isLoading = false;
            this.isError = true;
          }.bind(this)
        );
    },
  },
};
</script>
