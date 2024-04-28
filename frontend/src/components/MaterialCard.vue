<template>
  <div :class="`relative flex flex-col mt-6 text-gray-200 ${this.color} shadow-md bg-clip-border rounded-xl w-96 uppercase`">
  <div class="p-2 w-full">
      <h5 class="block font-sans text-xl antialiased font-semibold leading-snug tracking-normal text-blue-gray-900 text-center">
          {{ title }}
        </h5>
    <div class="flex justify-center items-center w-full">
        <BaseIcon :name="icon_name" class="w-24 h-24"/>
    </div>
    <p class="font-monster antialiased font-light text-center leading-relaxed text-inherit text-4xl">
      {{ value }}
    </p>
  </div>

</div> 
</template>

<script>
import BaseIcon from './BaseIcon.vue'
export default {
    props: {
        icon_name: String,
        title: String,
        value: Number,
        color: String
    },

    components: {
        BaseIcon
    }
}
</script>

<style>

</style>