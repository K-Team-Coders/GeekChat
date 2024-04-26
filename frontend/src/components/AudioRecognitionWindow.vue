<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="duration-500 min-h-[90vh] flex flex-col justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <div class="flex mb-4 pt-10">
        <p
          class="text-center text-4xl font-black font-mono text-activeText duration-500"
        >
          Преобразовать речь в текст
        </p>
      </div>
      <div :class="classes">
        <form>
          <div class="flex justify-start items-end">
            <input
              class="w-[92%] text-sm text-inputText duration-500 shadow-md border-[0.5px] py-1 px-2 border-inputBorder rounded-lg cursor-pointer bg-inputBackground focus:outline-none"
              aria-describedby="file_input_help"
              id="files"
              ref="files"
              type="file"
              accept="audio/*, video/*"
              @change="handleFilesUpload()"
            />
            <p
              class="w-[8%] mt-2.5 ml-2 text-sm text-activeText text-end duration-500"
              id="file_input_help"
            >
              .mp3 .wav
            </p>
          </div>
          <div class="flex justify-end pt-2">
            <button
              @click.prevent="submitFiles"
              type="submit"
              class="text-activeText duration-500 shadow-md bg-buttonBackground hover:bg-buttonHover focus:ring-4 focus:outline-none focus:ring-buttonBackground font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center mt-2"
            >
              Отправить файл
            </button>
          </div>
        </form>
        <div class="pt-4">
          <transition
            enter-active-class="transition-opacity easy-linear duration-500"
            enter-from-class="opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="transition-opacity easy-linear duration-500"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
          >
            <div
              class="flex flex-col justify-center gap-2 mb-10"
              v-if="isVideo"
            >
              <div
                class="flex justify-center w-full min-h-[323px] max-h-[600px] rounded-xl border-2 duration-500 border-outputBorder bg-outputBackground p-4"
                v-for="file in files"
                :key="file"
              >
                <video :src="url" type="video/mp4" controls></video>
              </div>

              <div class="w-full">
                <div class="flex justify-center pt-20">
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
                <TextOutput
                  v-if="isReady"
                  :text="text_massage"
                  :language="text_language"
                />
              </div>
            </div>
          </transition>
          <transition
            enter-active-class="transition-opacity easy-linear duration-500"
            enter-from-class="opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="transition-opacity easy-linear duration-500"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
          >
            <div :class="audioClasses" v-if="isAudio">
              <div class="w-full">
                <audio
                  controls
                  class="w-full"
                  v-for="file in files"
                  :key="file"
                >
                  <source :src="url" type="audio/mpeg" />
                </audio>
              </div>
              <div>
                <div class="flex justify-center pt-32">
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

                <TextOutput
                  :text="text_massage"
                  :language="text_language"
                  v-if="isReady"
                />
                <div class="pt-3"></div>
              </div>
            </div>
          </transition>
        </div>
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
    SidebarMain,
    TranslaterLoader,
    Alert,
  },
  data() {
    return {
      isVideo: false,
      isAudio: false,
      uploadFile: "",
      files: [],
      url: "",
      text_language: "",
      text_massage: "",
      isLoading: false,
      isReady: false,
      isError: false,
    };
  },
  computed: {
    classes() {
      return this.isVideo ? "w-8/12" : ["w-8/12", "h-[570px]", "pt-8"];
    },
    audioClasses() {
      return this.isAudio
        ? ["flex", "flex-col", "mb-[600px]", "pt-8"]
        : ["flex", "flex-col", "pt-8"];
    },
  },
  methods: {
    handleFilesUpload() {
      this.uploadFile = this.$refs.files.files[0];
      this.url = URL.createObjectURL(this.uploadFile);
      this.files.push(this.uploadFile.name);
      console.log(this.files);
      if (this.uploadFile.type.startsWith("video")) {
        this.isVideo = true;
        this.isAudio = false;
      } else if (this.uploadFile.type.startsWith("audio")) {
        this.isAudio = true;
        this.isVideo = false;
      }
    },
    async submitFiles() {
      this.isLoading = true;
      const formData = new FormData();
      formData.append("file", this.uploadFile);
      console.log(formData);
      axios
        .post(
          `http://${process.env.VUE_APP_AUDIOREC_SERVICE_IP}/audio_sample`,
          formData,
          {
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

<style></style>
