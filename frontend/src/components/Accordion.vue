<template>
  <div>
    <div class="text-activeText">
      <button
        @click.stop="this.isOpen = !this.isOpen"
        type="button"
        class="flex items-center justify-between w-full p-4 font-medium rtl:text-right border border-b-0 border-gray-200 rounded-t-xl focus:ring-0 gap-3"
      >
        <span>Выбранные языки: {{ language }}</span>
        <svg
          data-accordion-icon
          class="w-3 h-3 rotate-180 shrink-0"
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 10 6"
        >
          <path
            stroke="currentColor"
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 5 5 1 1 5"
          />
        </svg>
      </button>
      <transition
        enter-active-class="transition ease-out duration-100 "
        enter-from-class="transition opacity-0 scale-95"
        enter-to-class="transform opacity-100 scale-100"
        leave-active-class="transition ease-in duration-100"
        leave-from-class="transform opacity-100 scale-100"
        leave-to-class="tranfrom opacity-0 scale-95"
      >
        <div v-show="isOpen" class="">
          <div class="p-4 w-full border border-gray-200 rounded-b-lg">
            <ul
              class="items-center w-full text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-lg sm:flex dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            >
              <li
                class="w-full border-b border-gray-200 sm:border-b-0 sm:border-r dark:border-gray-600 grid grid-cols-4"
              >
                <div class="flex items-center ps-3" v-for="language in 50">
                  <input
                    id="vue-checkbox-list"
                    type="checkbox"
                    value=""
                    
                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                  />
                  <label
                    for="vue-checkbox-list"
                    class="w-full py-3 ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >{{ language }}</label
                  >
                </div>
              </li>
            </ul>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isOpen: true,
    };
  },
};
</script>
