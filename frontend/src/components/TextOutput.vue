<template>
  <div class="duration-500">
    <div
      class="h-full w-full border-[2px] duration-500 border-outputBorder bg-frameBackground rounded-lg p-4 mb-1 flex flex-col max-h-[600px]"
    >
      <p class="text-activeText text-bold duration-500">Содержимое файла:</p>
      <p class="text-activeText duration-500">{{ text }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    text: String,
  },
};
</script>

<style></style>
