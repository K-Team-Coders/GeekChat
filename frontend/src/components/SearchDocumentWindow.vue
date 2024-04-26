<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="flex flex-col duration-500 justify-center ml-72 items-center w-full bg-frameBackground rounded-xl outline-dashed outline-[1px] outline-outlineColor"
    >
      <div class="flex mb-4 pt-10">
        <p
          class="text-center text-4xl font-black font-mono text-activeText duration-500"
        >
          Документы
        </p>
      </div>
      <div class="w-5/6">
        <div class="flex">
          <div
            class="relative mb-4 flex w-full duration-500 flex-wrap items-stretch gap-2 justify-center text-activeText"
          >
            <SwitchToogle
              class="flex justify-end"
              v-model:checked="isSemanticSearch"
              :label="'Семантический поиск'"
            />
            <input
              @input="text_processing()"
              v-model="searchQuerry"
              type="search"
              class="relative shadow-md m-0 block min-w-0 flex-auto rounded border border-solid border-inputBorder bg-transparent bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-activeText outline-none transition duration-500 ease-in-out focus:z-[3] focus:border-primary focus:text-activeText focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none placeholder:text-activeText focus:border-primary"
              placeholder="Поиск"
              aria-label="Search"
              aria-describedby="button-addon2"
            />
          </div>
        </div>
      </div>
      <div class="w-5/6 flex justify-start items-center gap-4">
        <p class="text-xl text-activeText duration-500">Сортировка по:</p>
        <div class="flex justify-center gap-2 items-center pt-1">
          <select
            class="dark:bg-inputBackground bg-neutral-300 hover:bg-neutral-200 duration-300 rounded-xl px-4 py-1"
            v-model="selectedFilter"
            @change="filterDocsByCategory(selectedFilter)"
          >
            <option value="">Все категории</option>
            <option
              v-for="category in categories"
              :key="category.id"
              :value="category.id"
            >
              {{ category.name }}
            </option>
          </select>
        </div>
      </div>
      <div class="flex justify-end pt-12 w-5/6">
        <input
          @change="handleFilesUpload"
          type="file"
          accept=".doc,.docx"
          multiple
          hidden
          ref="uploadFile"
        />
        <div
          @click="$refs.uploadFile.click()"
          class="text-activeText dark:text-neutral-100 shadow-md items-center flex gap-2 border-[1px] border-outputBorder hover:bg-buttonHover hover:text-contrast cursor-pointer font-roboto font-medium px-4 py-2 rounded-l-xl duration-500"
        >
          Выбрать файлы
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-5 h-5"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M12 4.5v15m7.5-7.5h-15"
            />
          </svg>
        </div>
        <transition
          enter-active-class="transition ease-in-out duration-500 transform"
          enter-from-class="translate-x-full"
          enter-to-class="translate-x-0"
          leave-active-class="transition ease-in-out duration-500 transform"
          leave-from-class="translate-x-0"
          leave-to-class="translate-x-full"
        >
          <AlertisReady v-if="isUpload" @close="isUpload = false"
        /></transition>
        <div
          @click="submitFiles()"
          class="hover:bg-buttonHover shadow-md items-center text-neutral-100 flex gap-2 dark:bg-green-700 border-[1px] border-outputBorder font-roboto cursor-pointer font-medium px-4 py-2 rounded-r-xl duration-500 dark:hover:bg-green-800"
        >
          Загрузить
        </div>
      </div>
      <div class="w-5/6 flex justify-end pt-2">
        <div>
          <div class="text-neutral-100" v-for="(file, index) in file_list">
            {{ index + 1 }}. {{ file.name }}
          </div>
        </div>
      </div>
      <div class="w-5/6 mb-10">
        <div class="flex justify-center pt-4">
          <SmallLoader v-if="textisProcessing" />
        </div>
        <div class="flex justify-center pt-3" v-for="name in docs">
          <transition-group
            enter-active-class="transition ease-in-out duration-500 transform"
            enter-from-class="-translate-y-full"
            enter-to-class="translate-y-0"
            leave-active-class="transition ease-in-out duration-500 transform"
            leave-from-class="translate-y-0"
            leave-to-class="translate-y-full"
          >
            <div
              class="border-2 shadow-md border-neutral-200 w-full rounded-xl p-3"
            >
              <div class="flex items-center justify-between">
                <p
                  class="text-activeText text-xl hover:underline duration-500 cursor-pointer flex"
                  @click="getfilesByCreated(name)"
                >
                  {{ name }}
                </p>
                <BaseIcon
                  @click="deleteDocs(name, $event.target.closest('.border-2'))"
                  name="x"
                  class="w-5 h-5 text-activeText cursor-pointer hover:text-red-600 duration-500"
                />
              </div>
              <div class="flex justify-end items-end pt-3">
                <button
                  @click="getfilesByCreated(name)"
                  class="text-activeText hover:text-black dark:text-neutral-100 bg-buttonBackground font-roboto font-bold border-outputBorder hover:border-activeText border-2 px-5 py-2 rounded-xl hover:bg-buttonHover hover:text-contrast duration-500"
                >
                  Скачать
                </button>
              </div>
            </div>
          </transition-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import TextOutput from "./TextOutput.vue";
import SmallLoader from "./SmallLoader.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
import axios from "axios";
import debounce from "lodash/debounce";
import SwitchToogle from "./SwitchToogle.vue";
import AlertisReady from "./AlertisReady.vue";

export default {
  components: {
    TextOutput,
    SmallLoader,
    BaseIcon,
    SidebarMain,
    SwitchToogle,
    AlertisReady,
  },

  props: {
    text: { type: String, default: "" },
  },

  computed: {
    file_list() {
      return this.files;
    },

    makeSearchQuerry() {
      return this.searchQuerry;
    },
  },


  data() {
    return {
      categories: [
        { id: 1, name: "По названию А → Я" },
        { id: 2, name: "По названию Я → A" },
      ],
      filterIsOpen: false,
      searchQuerry: "",
      isSemanticSearch: true,
      documents: [],
      selectedFilter: null,
      files: [],
      docs: [],
      isLoading: false,
      isReady: false,
      isError: false,
      textisProcessing: false,
      language: "русский",
      downloadUrl: "",
      isUpload: false,
      documentBlock: true,
    };
  },


  created() {
    this.searchQuerry = this.$route.query.text;
  },

  methods: {
    submitFiles() {
      const formData = new FormData();
      for (let i = 0; i < this.files.length; i++) {
        formData.append("files", this.files[i]);
        formData.append("languages", this.language);
      }
      axios
        .post(
          "http://" + process.env.VUE_APP_DOC_SEARCH_IP + "/upload_files",
          formData
        )
        .then((response) => {
          console.log("Загружено:", response.data);
          this.isUpload = true;
        })
        .catch((error) => {
          console.error(error);
        });
    },

    handleFilesUpload(event) {
      this.files = event.target.files;
      console.log(this.files);
    },

    deleteDocs(name, documentBlock) {
      axios
        .delete(
          `http://${process.env.VUE_APP_DOC_SEARCH_IP}/delete_document/${name}`
        )

        .then(() => {
          this.documentBlock = null;
          // Удаление блока документа
          this.$nextTick(() => {
            if (documentBlock) {
              documentBlock.remove();
            }
          });
        })
        .catch((error) => {
          console.error(error);
        });
    },

    async getfilesByCreated(name) {
      this.isLoading = true;
      this.isError = false;

      try {
        const response = await axios.get(
          `http://${process.env.VUE_APP_DOC_SEARCH_IP}/get_document_from_db/${name}`,

          {
            responseType: "blob", // указываем, что ожидается объект Blob в ответе
          }
        );
        this.documents = response.data;
        console.log(this.documents);
        this.downloadFile(response.data, name);
      } catch (error) {
        this.isLoading = false;
        this.isError = true;
        console.log(error.response);
        this.error_info =
          error.response && error.response.data
            ? error.response.data
            : error.message;
      } finally {
        this.isLoading = false;
      }
    },
    downloadFile(blob, fileName) {
      // создаем новый элемент <a>
      const link = document.createElement("a");

      // устанавливаем свойству href значение объекта Blob
      link.href = window.URL.createObjectURL(blob);

      // устанавливаем атрибут download для скачивания файла
      link.setAttribute("download", fileName);

      // вызываем клик по ссылке
      link.click();
    },

    debounceStopTyping: debounce(function () {
      this.isTyping = false;
    }, 500),

    text_processing() {
      // this.isError = false;
      this.isTyping = true;
      this.textisProcessing = true;
      this.debounceStopTyping();
      this.docs = null;
      console.log(typeof this.searchQuerry);
      setTimeout(() => {
        if (this.isTyping == false && this.isSemanticSearch) {
          axios
            .post(
              `http://${process.env.VUE_APP_DOC_SEARCH_IP}/semantic_search`,
              { query: this.searchQuerry }
            )
            .then((response) => {
              this.docs = response.data;
              this.textisProcessing = false;
              console.log(this.docs);
            })
            .catch(function () {
              console.log("Ошибка");
              this.textisProcessing = false;
              // this.isError = true;
            });
        } else {
          axios
            .post(
              `http://${process.env.VUE_APP_DOC_SEARCH_IP}/full_text_search`,
              { query: this.searchQuerry }
            )
            .then((response) => {
              this.docs = response.data;
              this.textisProcessing = false;
              console.log(this.docs);
            })
            .catch(function () {
              console.log("Ошибка");
              this.textisProcessing = false;
              // this.isError = true;
            });
        }
      }, 2000);
    },

    filterDocsByCategory(categoryId) {
      let documents = this.docs
      if (!categoryId) {
        return;
      }
      switch (categoryId) {
        case 1:
          return documents.sort()
        case 2:
          return documents.sort().reverse()
        default:
          return true;
      }
    },
  },
  watch: {
    selectedFilter(newValue) {
      this.filterDocsByCategory(newValue);
    },
  },
};
</script>
