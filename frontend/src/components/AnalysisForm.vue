<script setup>
import { reactive, ref, computed } from 'vue';

const emit = defineEmits(['analysis-start', 'analysis-complete']);

const isLoading = ref(false);
const errorMessage = ref('');
const successMessage = ref('');


const weights = reactive({
  solar: 0.35,
  area: 0.25,
  grid: 0.20,
  slope: 0.15,
  infrastructure: 0.05,
});


const totalWeight = computed(() => {
  return (
    Number(weights.solar) +
    Number(weights.area) +
    Number(weights.grid) +
    Number(weights.slope) +
    Number(weights.infrastructure)
  );
});

// This check is now robust
const isInvalid = computed(() => {
  return Math.abs(totalWeight.value - 1.0) > 0.001;
});

async function runAnalysis() {
  if (isInvalid.value) {
    errorMessage.value = `Total weights must sum to 1.0. Current total: ${totalWeight.value.toFixed(2)}`;
    return;
  }
  
  isLoading.value = true;
  errorMessage.value = '';
  successMessage.value = '';
  emit('analysis-start');

  try {
    const response = await fetch('/api/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      // Pydantic is expecting {"weights": {"solar": 0.35, ...}}
      body: JSON.stringify({ weights: weights }),
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      
      if (Array.isArray(errorData.detail)) {
        // Just show the first error message
        throw new Error(errorData.detail[0].msg);
      } else {
        throw new Error(errorData.detail || 'Analysis failed');
      }
    }
    
    successMessage.value = "Analysis complete! Dashboard is refreshing...";
    emit('analysis-complete'); 
    
  } catch (error) {

    errorMessage.value = error.message;
  } finally {
    isLoading.value = false;
    setTimeout(() => { successMessage.value = ''; }, 3000);
  }
}
</script>

<template>
  <section class="card analysis-card">
    <form @submit.prevent="runAnalysis" class="analysis-form">
      <div class="form-header">
        <h3>Analysis Weights</h3>
        <div class="total-weight" :class="{ 'invalid': isInvalid }">
          Total: {{ totalWeight.toFixed(2) }} / 1.00
        </div>
      </div>
      
      <div class="sliders-grid">
        <!-- Solar -->
        <div class="form-group">
          <label for="solar">Solar ({{ (Number(weights.solar) * 100).toFixed(0) }}%)</label>
          <input type="range" id="solar" v-model.number="weights.solar" min="0" max="1" step="0.01" />
        </div>
        <!-- Area -->
        <div class="form-group">
          <label for="area">Area ({{ (Number(weights.area) * 100).toFixed(0) }}%)</label>
          <input type="range" id="area" v-model.number="weights.area" min="0" max="1" step="0.01" />
        </div>
        <!-- Grid -->
        <div class="form-group">
          <label for="grid">Grid ({{ (Number(weights.grid) * 100).toFixed(0) }}%)</label>
          <input type="range" id="grid" v-model.number="weights.grid" min="0" max="1" step="0.01" />
        </div>
        <!-- Slope -->
        <div class="form-group">
          <label for="slope">Slope ({{ (Number(weights.slope) * 100).toFixed(0) }}%)</label>
          <input type="range" id="slope" v-model.number="weights.slope" min="0" max="1" step="0.01" />
        </div>
        <!-- Infrastructure -->
        <div class="form-group">
          <label for="infra">Infra ({{ (Number(weights.infrastructure) * 100).toFixed(0) }}%)</label>
          <input type="range" id="infra" v-model.number="weights.infrastructure" min="0" max="1" step="0.01" />
        </div>
      </div>
      
      <div class="form-actions">
        <button type="submit" class="btn-primary" :disabled="isLoading || isInvalid">
          {{ isLoading ? 'Analyzing...' : 'Re-Analyze Scores' }}
        </button>
      </div>
      
      <div v-if="errorMessage" class="message error-message">{{ errorMessage }}</div>
      <div v-if="successMessage" class="message success-message">{{ successMessage }}</div>
    </form>
  </section>
</template>

<style scoped>
.analysis-card {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
}
.form-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}
.form-header h3 {
  margin: 0;
}
.total-weight {
  font-weight: 600;
  color: #2ecc71;
  background: #e8f8f0;
  padding: 0.25rem 0.75rem;
  border-radius: 6px;
}
.total-weight.invalid {
  color: #e74c3c;
  background: #fbebee;
}

.sliders-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}
.form-group {
  display: flex;
  flex-direction: column;
}
.form-group label {
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  color: #555;
}
.form-group input[type="range"] {
  width: 100%;
  cursor: grab;
}
.form-group input[type="range"]:active {
  cursor: grabbing;
}

.form-actions {
  display: flex;
}
button {
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 600;
  transition: background-color 0.2s;
}
.btn-primary {
  background-color: #3498db;
  color: white;
}
.btn-primary:hover {
  background-color: #2980b9;
}
.btn-primary:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.message {
  margin-top: 1rem;
  padding: 0.75rem;
  border-radius: 6px;
  font-size: 0.9rem;
  text-align: center;
}
.error-message {
  background-color: #fbebee;
  color: #c0392b;
}
.success-message {
  background-color: #e8f8f0;
  color: #27ae60;
}
</style>