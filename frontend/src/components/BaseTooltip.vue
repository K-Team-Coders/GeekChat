<template>
  <div class="relative">
    <div
      class="h-full flex items-center"
      @mouseenter="isShowm = true"
      @mouseleave="isShowm = false"
      @click="isShowm = false"
    >
      <slot />
    </div>
    <transition
      enter-active-class="duration-300 "
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="duration-80"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-show="isShowm" :class="classes">{{ text }}</div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isShowm: false,
    };
  },

  props: {
    text: String,
    top: Boolean,
    left: Boolean,
    right: Boolean,
  },

  methods: {
    getPositionClasses() {
      const topClass = this.top ? "bottom-12" : "-top-8";

      if (this.right) {
        return [topClass, "left-10"];
      }

      if (this.left) {
        return [topClass, "right-0"];
      }
      return [topClass, "-translate-x-1/2", "left-1/2"];
    },
  },

  computed: {
    classes() {
      return [
        "bg-black",
        "bg-opacity-80",
        "rounded-lg",
        "text-white",
        "text-xs",
        "whitespace-nowrap",
        "p-2",
        "absolute",
        "transform",
        "bottom-2",
        "right-14"
      ];
    },
  },
};
</script>
