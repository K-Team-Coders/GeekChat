<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="flex min-h-[92vh] flex-col duration-500 pt-4 ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <div class="flex mb-4 pt-10">
        <p
          class="text-center text-4xl font-black font-mono text-activeText duration-500"
        >
          Узнать об объекте с фотографии
        </p>
      </div>
      <div class="w-10/12">
        <form>
          <div class="flex justify-start items-center">
            <input
              class="w-full duration-500 text-sm text-inputText shadow-md border-[0.5px] py-1 px-2 border-inputBorder rounded-lg cursor-pointer bg-inputBackground focus:outline-none"
              aria-describedby="file_input_help"
              id="files"
              ref="files"
              type="file"
              accept="image/png, image/jpeg"
              @change="handleFilesUpload()"
            />
            <p
              class="w-[8%] mt-2.5 ml-2 text-sm text-activeText text-end duration-500"
              id="file_input_help"
            >
              .jpeg .jpg
            </p>
          </div>
          <div class="flex justify-end pt-2">
            <button
              @click.prevent="scrollToBottom"
              type="submit"
              class="text-activeText shadow-md bg-buttonBackground hover:bg-buttonHover duration-500 focus:ring-4 focus:outline-none focus:ring-buttonBackground font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center mt-2"
            >
              Отправить файл
            </button>
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
          <div class="flex flex-col justify-center gap-2 items-center">
            <div
              v-if="isPhoto"
              class="flex min-w-[200px] max-w-[70vw] duration-500 min-h-[323px] max-h-[800px] rounded-xl border-2 border-outputBorder bg-outputBackground p-4"
              v-for="file in files"
              :key="file"
            >
              <img :src="url" />
            </div>
            <div class="w-full py-4">
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
              <div
                class="flex justify-center pt-2 w-full gap-2 px-4"
                v-show="isReady"
              >
                <canvas
                  class="min-w-[200px] max-w-[50vw] duration-500 min-h-[323px] max-h-[800px] rounded-xl border-2 border-outputBorder bg-outputBackground p-4"
                  id="canvas"
                ></canvas>
                <div>
                  <TextOutput :text="caption.russian" />
                  <div>
                    <ul
                      class="text-activeText border-2 border-outputBorder rounded-xl p-4"
                      v-for="(class_element, index) in recognition"
                      :key="index"
                    >
                      <p>Класс: {{ class_element.class_name }}</p>
                      <p>
                        Подклассы:
                        <li
                          class="ml-5"
                          v-for="(
                            subclass_element, index
                          ) in class_element.subclass_info"
                          :key="index"
                        >
                          {{ index + 1 }}. {{ subclass_element.name }}
                        </li>
                      </p>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </transition>
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
      url: "",
      files: [],
      caption: "",
      recognition: {},
      isError: false,
      isLoading: false,
      isReady: false,
      classColor: [],
    };
  },
  methods: {
    handleFilesUpload() {
      this.files = [];
      this.isReady = false;
      this.uploadFile = this.$refs.files.files[0];
      const typeFile = this.uploadFile.type;
      this.url = URL.createObjectURL(this.uploadFile);
      console.log(typeFile);
      this.files.push(this.uploadFile.name);
      console.log(this.files);
      if (this.uploadFile.type.startsWith("image")) {
        this.isPhoto = true;
      } else {
        this.isPhoto = false;
      }
    },

    getRandomColor() {
      return "#" + Math.floor(Math.random() * 16777215).toString(16);
    },

    drawImage(recognition) {
      const canvas = document.getElementById("canvas");
      const context = canvas.getContext("2d");
      const img = new Image();
      img.src = this.url;
      img.onload = () => {
        canvas.width = img.width;
        canvas.height = img.height;
        context.lineWidth = 3;
        context.drawImage(img, 0, 0);

        recognition.forEach((element) => {
          context.beginPath();
          let randomColor = this.getRandomColor();
          context.strokeStyle = randomColor;
          context.fillStyle = randomColor;
          this.classColor.push(randomColor);
          console.log(`Случайный цвет ${context.strokeStyle}`);
          element.subclass_info.forEach((subclass_element) => {
            let coords = subclass_element.coords;
            let x = coords[0];
            let y = coords[1];
            let width = coords[2] - coords[0];
            let height = coords[3] - coords[1];
            context.font = `15px white bold Arial`;
            context.rect(x, y, width, height);
            context.fillStyle = randomColor;
            context.fillRect(x - 2, y - 35, width + 5, 35);
            context.stroke();
            context.fillStyle = "#FFFFFF";
            context.fillText(`ПОДКЛАСС: ${subclass_element.name}`, x, y - 3);
            context.fillText(`КЛАСС: ${element.class_name}`, x, y - 15);
          });
          context.closePath();
        });
      };
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
      console.log(formData);
      axios
        .post(
          `http://${process.env.VUE_APP_IMAGE_TO_TEXT_SERVICE_IP}/image_caption`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then((response) => {
          this.caption = response.data.caption;
          this.recognition = response.data.recognition;
          this.isLoading = false;
          this.isReady = true;
          this.isPhoto = false;
          this.drawImage(this.recognition);
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

<style scoped></style>
