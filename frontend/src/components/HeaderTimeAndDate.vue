<template>
  <div class="dark:text-white text-center text-neutral-600 duration-300 text-2xl">
    <p class="text-7xl font-monster">
      {{ localeTime }}
    </p>
    <p class="text-lg font-monster">
      {{ localeDate }}
    </p>
  </div>
</template>

<script>
export default {
  data: () => ({
    date: new Date(),
  }),

  computed: {
    localeDate() {
      return this.date.toLocaleDateString("ru-RU", {
        weekday: "long",
        month: "long",
        day: "numeric",
      });
    },
    localeTime() {
      return this.date.toLocaleTimeString("ru-RU", {
        hour: "2-digit",
        minute: "2-digit",
      });
    },
  },

  created() {
    this.intervalId = setInterval(() => (this.date = new Date()), 1000);
  },

  beforeDestroy() {
    if (this.intervalId) clearInterval(this.intervalId);
  },
};
</script>
