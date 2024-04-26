<template>
  <router-link :to="`${url}`">
    <div
      class="duration-300 dark:bg-[#ededed] rounded-[10px] border-[1.5px] dark:hover:text-red-600 hover:text-blue-600 border-[#909090] bg-background dark:hover:shadow-lg dark:hover:shadow-red-900 hover:shadow-4xl"
    >
      <div class="w-full rounded-[10px] duration-300 cursor-pointer">
        <div class="flex flex-col justify h-36">
          <div class="flex justify-center pt-4">
            <BaseIcon
              :name="name"
              class="w-14 h-14 ml-3 hover:text-inherit text-neutral-600 duration-300"
            />
          </div>
          <p
            class="text-neutral-600 uppercase w-full duration-500 px-2 font-semibold text-center text-sm h-full py-2.5"
          >
            {{ title }}
          </p>
        </div>
      </div>
    </div>
  </router-link>
</template>
<script>
import BaseIcon from "@/components/BaseIcon.vue";

export default {
  props: {
    title: String,
    url: String,
    name: String,
  },
  components: { BaseIcon },
};
</script>
