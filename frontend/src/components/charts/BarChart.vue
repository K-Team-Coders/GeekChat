<template>
  <div class="text-center">
    <Bar :chart-data="chartData" :chart-options="chartOptions" />
    {{ description }}
  </div>
  
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  props: {
    dataset: Object,
    description: String
  },
  name: 'BarChart',
  components: { Bar },
 
  data() {
    return {
      name_set: [],
      pos_set: [],
      neu_set: [],
      neg_set: [],
      chartData: {
        labels: [],

        datasets: [
          {
            label: 'Положительных',
            backgroundColor: '#00cf00',
            data: [],

          },
          {
            label: 'Нейтральных',
            backgroundColor: '#D0D0D0',
            data: []
          },
          {
            label: 'Негативных',
            backgroundColor: 'red',
            data: []
          }
        ]
      },
      chartOptions: {
        stacked: true
      }
    }
  }
}
</script>