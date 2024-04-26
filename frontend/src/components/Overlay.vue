<template>
  <div class="fixed bottom-4 right-4 items-center">
    <BaseTooltip text="Пересказать текст можем, поможем!">
      <button>
        <transition
          enter-active-class="transition ease-in-out duration-700 transform"
          enter-from-class="translate-x-full translate-x-full"
          enter-to-class="translate-x-0"
          leave-active-class="transition ease-in-out duration-700 transform"
          leave-from-class="translate-x-0"
          leave-to-class="translate-x-full translate-x-full"
        >
          <ModalWindow
            style="z-index: 9999"
            v-if="isModalOpen"
            @close="isModalOpen = false"
          />
        </transition>
      </button>
      <div
        class="w-12 h-12 bg-neutral-300 rounded-full flex justify-center items-center hover:bg-neutral-400 duration-300 hover:-translate-x-1"
        @click="isModalOpen = true"
      >
        <BaseIcon
          name="story"
          @click="isModalOpen = true"
          class="w-6 h-6 text-neutral-600 cursor-pointer"
        />
      </div>
    </BaseTooltip>
  </div>
</template>
<script>
import BaseIcon from "./BaseIcon.vue";
import BaseTooltip from "./BaseTooltip.vue";
import ModalWindow from "./ModalWindow.vue";

export default {
  components: { BaseIcon, BaseTooltip, ModalWindow },
  data() {
    return {
      isModalOpen: false,
    };
  },
  emits: ["close"],
};
</script>
