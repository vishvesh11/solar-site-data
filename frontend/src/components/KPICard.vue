<script setup>
defineProps({
  title: String,
  value: [String, Number],
  unit: {
    type: String,
    default: ''
  }
});
</script>

<template>
  <div class="kpi-card">
    <span class="title">{{ title }}</span>
    <div class="value-container">
      <span class="value">{{ value }}</span>
      <span class="unit">{{ unit }}</span>
    </div>
  </div>
</template>

<style scoped>
.kpi-card {
  background: #fff;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}
.title {
  font-size: 0.9rem;
  color: #667;
  display: block;
  margin-bottom: 0.5rem;
}
.value-container {
  display: flex;
  align-items: flex-end;
}
.value {
  font-size: 2rem;
  font-weight: 600;
  color: #333;
  line-height: 1;
}
.unit {
  font-size: 1rem;
  font-weight: 500;
  color: #555;
  margin-left: 0.5rem;
  padding-bottom: 2px; 
  
}
</style>