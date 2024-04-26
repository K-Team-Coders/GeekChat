<template>
  <div>
    <nav class="flex duration-500">
      <div
        class="flex gap-3 text-xl text-activeText duration-500 justify-end font-semibold p-4"
      >
        <router-link to="/">
          <ul class="hover:text-unactiveText duration-500">
            Главная
          </ul>
        </router-link>
        <router-link to="/allservices" class="hover:text-unactiveText duration-500">
          Cервисы
        </router-link>
      </div>
    </nav>
  </div>
</template>

<script>
export default {};
</script>
