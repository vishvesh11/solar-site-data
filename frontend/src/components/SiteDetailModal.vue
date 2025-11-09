<script setup>
import { computed, watch } from 'vue';

const props = defineProps({
  site: Object, 
  show: Boolean,
});
const emit = defineEmits(['close']);


const scoreBreakdown = computed(() => {
  if (!props.site) return [];
  return [
    { name: 'Solar Irradiance', value: props.site.solar_irradiance_score, weight: '35%' },
    { name: 'Available Area', value: props.site.area_score, weight: '25%' },
    { name: 'Grid Distance', value: props.site.grid_distance_score, weight: '20%' },
    { name: 'Terrain Slope', value: props.site.slope_score, weight: '15%' },
    { name: 'Infrastructure', value: props.site.infrastructure_score, weight: '5%' },
  ];
});


const siteData = computed(() => {
  if (!props.site) return [];
  return [
    { name: 'Region', value: props.site.region },
    { name: 'Coordinates', value: `${props.site.latitude.toFixed(4)}, ${props.site.longitude.toFixed(4)}` },
    { name: 'Area', value: `${props.site.area_sqm.toLocaleString()} m²` },
    { name: 'Solar (avg)', value: `${props.site.solar_irradiance_kwh} kWh/m²/day` },
    { name: 'Grid Distance', value: `${props.site.grid_distance_km} km` },
    { name: 'Slope', value: `${props.site.slope_degrees}°` },
    { name: 'Road Distance', value: `${props.site.road_distance_km} km` },
    { name: 'Land Type', value: props.site.land_type },
  ];
});


watch(() => props.show, (newVal) => {
  if (newVal) {
    document.body.classList.add('modal-open');
  } else {
    document.body.classList.remove('modal-open');
  }
});
</script>

<template>
  <Transition name="modal-fade">
    <div v-if="show" class="modal-backdrop" @click.self="emit('close')">
      
      <Transition name="modal-slide">
        <div v-if="show" class="modal-content hide-scrollbar">
          
          <div class="modal-header">
            <h2>{{ site.site_name }}</h2>
            <button @click="emit('close')" class="close-btn">&times;</button>
          </div>

          <div class="modal-body">
            <div class="score-highlight">
              <span>Total Score</span>
              <span class="total-score">{{ site.total_suitability_score.toFixed(1) }}</span>
            </div>
            
            <div class="grid-container">
              <div class="grid-col">
                <h3>Score Breakdown</h3>
                <ul class="score-list">
                  <li v-for="item in scoreBreakdown" :key="item.name">
                    <span class="score-name">{{ item.name }} ({{ item.weight }})</span>
                    <span class="score-value">{{ item.value.toFixed(1) }}</span>
                  </li>
                </ul>
              </div>
              
              <div class="grid-col">
                <h3>Site Data</h3>
                <ul class="data-list">
                  <li v-for="item in siteData" :key="item.name">
                    <span class="data-name">{{ item.name }}</span>
                    <span class="data-value">{{ item.value }}</span>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          
        </div>
      </Transition>
    </div>
  </Transition>
</template>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 600px;
  max-height: 80vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem;
  border-bottom: 1px solid #eee;
}
.modal-header h2 {
  margin: 0;
  font-size: 1.4rem;
  color: #333;
}
.close-btn {
  background: none;
  border: none;
  font-size: 2rem;
  font-weight: 300;
  color: #888;
  cursor: pointer;
  line-height: 1;
}

.modal-body {
  padding: 1.5rem;
}

.score-highlight {
  background-color: #f4f7fa;
  border-radius: 8px;
  padding: 1rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}
.score-highlight span {
  font-size: 1.1rem;
  font-weight: 600;
  color: #555;
}
.total-score {
  font-size: 2rem !important;
  font-weight: 700 !important;
  color: #3498db !important;
}

.grid-container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.grid-col h3 {
  font-size: 1.1rem;
  color: #555;
  margin-top: 0;
  margin-bottom: 1rem;
  border-bottom: 1px solid #eee;
  padding-bottom: 0.5rem;
}

.score-list, .data-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.score-list li, .data-list li {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
}
.score-name, .data-name {
  color: #667;
}
.score-value, .data-value {
  font-weight: 600;
  color: #333;
}
.score-value {
  color: #3498db;
}

/* Animations */
.modal-fade-enter-active,
.modal-fade-leave-active {
  transition: opacity 0.3s ease;
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
}

.modal-slide-enter-active,
.modal-slide-leave-active {
  transition: transform 0.3s ease-out;
}
.modal-slide-enter-from,
.modal-slide-leave-to {
  transform: translateY(-30px);
}
</style>