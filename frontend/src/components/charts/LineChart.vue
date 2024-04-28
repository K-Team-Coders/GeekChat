<template>
    <LineChartGenerator
      :chart-options="chartOptions"
      :chart-data="getData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
    />
  </template>
  
  <script>
  import { Line as LineChartGenerator } from 'vue-chartjs'
  
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    CategoryScale,
    PointElement
  } from 'chart.js'
  
  ChartJS.register(
    Title,
    Tooltip,
    Legend,
    LineElement,
    LinearScale,
    CategoryScale,
    PointElement
  )
  
  export default {
    name: 'LineChart',
    components: {
      LineChartGenerator
    },
    props: {
      chartId: {
        type: String,
        default: 'line-chart'
      },
      datasetIdKey: {
        type: String,
        default: 'label'
      },
      cssClasses: {
        default: 'dark:bg-stone-300 bg-slate-50',
        type: String
      },
      styles: {
        type: Object,
        default: () => {}
      },
      plugins: {
        type: Array,
        default: () => []
      },
      label: String,
      datasets: Array,
      color: String,
    },
    computed: {
      getData(){
        let chart = {
          labels: [
            '00:00 ',
            '01:00 ',
            '02:02 ',
            '03:02 ',
            '04:02 ',
            '05:02 ',
            '06:02 '
          ],
          datasets: [
            {
              label: this.label,
              backgroundColor: this.color,
              data: [1, 30, 25, 10, 7, 3, 0]
            }
          ]
        }
        return chart
      }
    },

    data() {
      return {
        chartData: {
          labels: [
            '00:00 ',
            '00:01 ',
            '00:02 ',
            '00:02 ',
            '00:02 ',
            '00:02 ',
            '00:02 '
          ],
          datasets: [
            {
              label: 'Уровень активности',
              backgroundColor: '#ed6a32',
              data: [1, 30, 25, 10, 7, 3, 0]
            }
          ]
        },
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false
        }
      }
    }
  }
  </script>
  