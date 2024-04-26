<template>
  <footer class="border-t-2 border-inputBorder duration-500">
    <div class="mx-auto w-full max-w-screen-xl p-4 py-6">
      <div class="md:flex md:justify-between">
        <div class="grid grid-cols-2 gap-8 sm:gap-6 sm:grid-cols-4">
          <div>
            <h2
              class="mb-6 text-sm font-semibold uppercase text-activeText duration-500"
            >
              Работа с текстом
            </h2>
            <ul class="text-unactiveText font-medium duration-500">
              <li class="mb-4">
                <router-link
                  to="/translater"
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Переводчик</router-link
                >
              </li>
              <li>
                <router-link
                  to="/text_to_audio"
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Преобразователь в аудио</router-link
                >
              </li>
            </ul>
          </div>
          <div>
            <h2
              class="mb-6 text-sm font-semibold uppercase text-activeText duration-500"
            >
              Работа с изображениями
            </h2>
            <ul class="text-unactiveText font-medium">
              <li class="mb-4">
                <router-link
                  to="/scan_from_docs"
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Распознаватель текста</router-link
                >
              </li>
              <li>
                <router-link
                  to=""
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Распознаватель объектов</router-link
                >
              </li>
            </ul>
          </div>
          <div>
            <h2
              class="mb-6 text-sm font-semibold uppercase text-activeText duration-500"
            >
              Работа с аудио
            </h2>
            <ul class="text-unactiveText font-medium duration-500">
              <li class="mb-4">
                <router-link
                  to="/audio_recognition"
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Распознаватель аудио</router-link
                >
              </li>
            </ul>
          </div>
          <div>
            <h2
              class="mb-6 text-sm font-semibold uppercase text-activeText duration-500"
            >
              Работа с документами
            </h2>
            <ul class="text-unactiveText font-medium">
              <li class="mb-4">
                <router-link
                  to=""
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Информационно-справочная система</router-link
                >
              </li>
              <li class="mb-4">
                <router-link
                  to=""
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Поиск документов</router-link
                >
              </li>
              <li class="mb-4">
                <router-link
                  to="/"
                  class="hover:underline hover:text-unactiveText duration-500"
                  >Формирование документов</router-link
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {};
</script>

<style></style>
