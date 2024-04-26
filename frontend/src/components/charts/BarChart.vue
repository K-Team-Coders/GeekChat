<template>
  <Bar :chart-data="chartData" :chart-options="chartOptions" />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  props: {
    dataset: Object
  },
  name: 'BarChart',
  components: { Bar },
  mounted() {
    console.log(this.dataset)
    let name_set = []
    let pos_set = []
    let neu_set = []
    let neg_set = []
    this.dataset.forEach(element => {
    name_set.push(element.cluster_name),
    pos_set.push( element.numPositive),
    neu_set.push( element.numNeutral),
    neg_set.push( element.numNegative)
    });
    this.chartData.labels = name_set
    this.chartData.datasets[0].data = pos_set
    this.chartData.datasets[1].data = neu_set
    this.chartData.datasets[2].data = neg_set
  },
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