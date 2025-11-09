<script setup>
import { computed } from 'vue';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const props = defineProps({
  sites: Array
});

const chartData = computed(() => {

  const bins = {
    '0-19 (Very Poor)': 0,
    '20-39 (Poor)': 0,
    '40-59 (Fair)': 0,
    '60-79 (Good)': 0,
    '80-100 (Excellent)': 0,
  };

  props.sites.forEach(site => {
    const score = site.total_suitability_score;
    if (score === null || score === undefined) return;
    
    if (score >= 80) bins['80-100 (Excellent)']++;
    else if (score >= 60) bins['60-79 (Good)']++;
    else if (score >= 40) bins['40-59 (Fair)']++;
    else if (score >= 20) bins['20-39 (Poor)']++;
    else bins['0-19 (Very Poor)']++;
  });

  return {
    labels: Object.keys(bins),
    datasets: [
      {
        label: 'Number of Sites',
        backgroundColor: [
          '#e74c3c', // red
          '#e67e22', // orange
          '#f1c40f', // yellow
          '#2ecc71', // green
          '#27ae60', // dark Green
        ],
        data: Object.values(bins),
      },
    ],
  };
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false, 
    },
  },
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: 'Number of Sites'
      }
    }
  }
};
</script>

<template>
  <div style="height: 100%; width: 100%;">
    <Bar v-if="sites && sites.length" :data="chartData" :options="chartOptions" />
    <div v-else class="no-data">
      No data to display in chart.
    </div>
  </div>
</template>

<style scoped>
.no-data {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #777;
}
</style>
