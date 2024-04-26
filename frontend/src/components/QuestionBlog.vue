<template>
  <div class="grid gap-2.5 px-2 2xl:grid-cols-4 xl:grid-cols-4 lg:grid-cols-3 md:grid-cols-2">
    <div v-if="isLoading">Загрузка</div>
    <div v-else @click="card_click(item.table_id)"
      class="bg-gray-50 h-[250px] py-2 font-bold text-idealblack text-start hover:border-blueGod cursor-pointer shadow-inner hover:text-activeText  hover:bg-orangeGod transition ease-in-out delay-50 relative"
      v-for="item in question_list" :key="item.table_id">
      <div class="flex flex-col mb-auto">
        <p class="ml-3 text-xl">
          {{ item.table_id }}
        </p>
        <p class="absolute bottom-[22px] right-[20px] top-auto left-[10px] sm:text-lg text-xs">
          {{ item.table_head_question }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  props: {
    question_list: Array,
  },
  data() {
    return {
      colors: ["#4487BE", "#FF7E00", "#222"],
      isLoading: false
    };
  },
  methods: {
    card_click(id) {
      this.isLoading = true;
      axios.post(`http://${process.env.VUE_APP_USER_IP_WITH_PORT}/tabledetailview/${id}/`)
        .then(console.log('Success'))
        .catch(function (response) {
          console.log("FAILURE!!");
          if (response.statusCode == 404) {
            this.$router.push(`/notfound`)
          }})
        .finally(() => {
				this.isLoading = false;
			});
        this.$router.push(`/answer/${id}`)

    }
  },
};
</script>

<style></style>
