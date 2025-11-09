<script setup>
import { reactive } from 'vue';

const emit = defineEmits(['filter-change']);

const formState = reactive({
  minScore: 0,
  maxScore: 100,
});

function applyFilters() {
  emit('filter-change', { ...formState });
}

function resetFilters() {
  formState.minScore = 0;
  formState.maxScore = 100;
  applyFilters();
}
</script>

<template>
  <section class="card filter-card">
    <h3>Filter Sites</h3>
    <form @submit.prevent="applyFilters" class="filter-form">
      <div class="form-group">
        <label for="minScore">Min Score ({{ formState.minScore }})</label>
        <input
          type="range"
          id="minScore"
          v-model.number="formState.minScore"
          min="0"
          max="100"
        />
      </div>
      <div class="form-group">
        <label for="maxScore">Max Score ({{ formState.maxScore }})</label>
        <input
          type="range"
          id="maxScore"
          v-model.number="formState.maxScore"
          min="0"
          max="100"
        />
      </div>
      <div class="form-actions">
        <button type="submit" class="btn-primary">Apply Filters</button>
        <button type="button" @click="resetFilters" class="btn-secondary">Reset</button>
      </div>
    </form>
  </section>
</template>

<style scoped>
.filter-card {
  margin-bottom: 1.5rem;
  padding: 1.5rem;
}
h3 {
  margin-top: 0;
  margin-bottom: 1rem;
}
.filter-form {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.5rem;
  align-items: flex-end;
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
}
.form-actions {
  display: flex;
  gap: 0.5rem;
}
button {
  padding: 0.75rem 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
}
.btn-primary {
  background-color: #3498db;
  color: white;
}
.btn-secondary {
  background-color: #ecf0f1;
  color: #333;
}
</style>