<template>
  <div
    class="fixed pt-3 inset-0 z-50 focus:outline-none duration-500"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div
      class="bg-neutral-100 rounded-lg max-w-md fixed bottom-2 right-4 xl:my-2 flex flex-col shadow-4xl"
    >

      <div class="">
        <ModalWindowButtonClose @click="close" class="absolute right-0" />
      </div>
      <div class="pt-10 flex justify-center">
        <div class="w-9/12 items-center flex flex-col">
          <p class="pb-3 font-bold text-xl">Пересказчик</p>
          <input
            class="w-full text-sm text-inputText shadow-md border-[0.5px] py-1 px-2 border-inputBorder rounded-lg cursor-pointer bg-inputBackground focus:outline-none"
            aria-describedby="file_input_help"
            id="files"
            ref="files"
            type="file"
            accept=".docs .doc"
            @change="handleFilesUpload()"
          />
          <div class="w-96">
            <p
              class="m-4 text-sm font-bold border-t-2 border-b-2 border-neutral-300"
            >
              или вставьте текст
            </p>
          </div>
          <div class="w-full">
            <textarea
              @input="text_processing()"
              ref="myinput"
              class="w-full custom-scrollbar shadow-md border-[0.5px] border-inputBorder duration-500 bg-inputBackground text-activeText text-sm pl-6 pt-4 pb-4 pr-14 min-h-[100px] text-wrap rounded-xl focus:outline-none focus:ring-0 focus:border-none text-start placeholder:text-unactiveText placeholder:text-sm"
              type="text"
              placeholder="Начните писать или вставьте текст"
            ></textarea>
          </div>
          <div class="pb-6">
            <button
              @click.prevent="scrollToBottom"
              type="submit"
              class="text-activeText shadow-md bg-buttonBackground hover:bg-buttonHover duration-500 focus:ring-4 focus:outline-none focus:ring-buttonBackground font-semibold rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center mt-2"
            >
              Отправить файл
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";

export default {
  components: {
    ModalWindowButtonClose,
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
  mounted() {
    this.$el.focus();
  },
  emits: ["close"],
};
</script>
