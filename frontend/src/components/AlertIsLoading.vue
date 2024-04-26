<template>
    <div class="fixed right-0 bottom-1 py-2 z-50">
      <div
        class="bg-blue-200 border-l-4 border-blue-500 text-blue-700 p-4 w-96"
        role="alert"
      >
        <div class="relative">
          <BaseIcon
            name="settings"
            class="w-6 h-6 absolute -right-2 -top-2"
            @click="$emit('close')"
          />
        </div>
        <p class="font-bold text-xl">Загрузка</p>
        <p class="text-lg">Подключение к серверу....</p>
      </div>
    </div>
  </template>
  <script>
  import BaseIcon from "./BaseIcon.vue";
  
  export default {
    components: { BaseIcon },
  };
  </script>
  