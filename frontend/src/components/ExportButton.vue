<script setup>
const props = defineProps({
  filters: Object, 
});

function exportData(format = 'csv') {

  const params = new URLSearchParams();
  params.append('format', format);
  if (props.filters.minScore > 0) {
    params.append('min_score', props.filters.minScore);
  }
  if (props.filters.maxScore < 100) {
    params.append('max_score', props.filters.maxScore);
  }
  

  const exportUrl = `/api/export?${params.toString()}`;
  window.open(exportUrl, '_blank');
}
</script>

<template>
  <button @click="exportData('csv')" class="btn-secondary">
    Export Filtered (CSV)
  </button>
</template>

<style scoped>
button {
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background-color 0.2s;
  background-color: #ecf0f1;
  color: #333;
}
button:hover {
  background-color: #bdc3c7;
}
</style>