<template>
  <div class="w-full py-2 duration-500">
    <TranslaterLoader v-if="is_Loading" class="flex justify-center "/>
    <form v-else action="">
      Перевод документа
      <div class="flex justify-start">
        <input
          v-on:change="handleFilesUpload()"
          class="w-full duration-500 shadow-md text-sm text-inputText border-[1px] border-inputBorder py-1 px-2 rounded-lg cursor-pointer bg-inputBackground focus:outline-none"
          aria-describedby="file_input_help"
          id="files"
          ref="files"
          type="file"
        />
      </div>
      <div class="flex justify-end pt-2">
        <button
          @click="submitFiles()"
          type="submit"
          class="text-activeText duration-500 shadow-md bg-buttonBackground hover:bg-buttonHover focus:ring-4 focus:outline-none focus:ring-buttonBackground font-semibold rounded-xl text-sm w-full sm:w-auto px-5 py-2.5 text-center"
        >
          Отправить файл
        </button>
      </div>
    </form>
    <div> 
     <output  v-if="is_Ready"
                  class="w-full h-48 rounded-br-xl text-activeText p-4 duration-500"
                  v-on:focus="$event.target.select()"
                  ref="myoutput"
                >
                  {{ text }}</output
                >
    </div>
  </div>
</template>
<script>
import axios from "axios";
import TranslaterLoader from "./TranslaterLoader.vue";

export default {
  components: {
    TranslaterLoader,
  },
  props: {
    url: String,
  },
  data() {
    return {
      is_Error: false,
      files: "",
      text: "",
      is_Loading: false,
      is_Ready: false,
      colors: ["#4487BE", "#FF7E00", "#222"],
    };
  },
  methods: {
    submitFiles() {
      console.log(this.files);
      this.is_Loading = true;
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append("file", file);
      }
      console.log(this.IP);
      axios
        .post(`http://${VUE_APP_TRANSLATE_SERVICE_IP}/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then(response =>  {
          this.is_Loading = false;
          this.is_Ready = true;
          console.log("Файл переведен!");
          console.log(response.data);
          this.text = response.data
        })
        .catch(function (response) {
          console.log("FAILURE!!");
          if (response.statusCode == 400) {
            alert("Такой файл уже был загружен! Загрузите другой.");
          }
        })
        .finally(function () {
          this.is_Loading = false;
        });
    },
    handleFilesUpload() {
      this.files = this.$refs.files.files;
    },
  },
};
</script>
