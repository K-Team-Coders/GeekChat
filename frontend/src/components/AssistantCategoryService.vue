<template>
  <div class="duration-500">
    <div
      class="py-2 flex gap-2 pl-3 text-left cursor-pointer text-base transition rounded-lg w-full hover:text-activeText items-center duration-500"
      :class="{
        'dark:bg-frameBackground bg-gray-300 text-activeText duration-500': isActive,
        'text-unactiveText duration-500': !isActive,
      }"
    >
      <div class="flex justify-center items-center mt-1.5">
        <BaseIcon :name="name" :class="classed" />
      </div>

      <div class="pl-0.5">
        {{ category }}
      </div>
    </div>
  </div>
</template>
<script>
import BaseIcon from "./BaseIcon.vue";

export default {
  props: ["category", "isActive", "name", "classed"],
  components: { BaseIcon },
};
</script>
