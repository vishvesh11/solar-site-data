<script setup>
import { ref, reactive, onMounted, computed } from 'vue';
import KPICard from '@/components/KPICard.vue';
import SiteMap from '@/components/SiteMap.vue';
import SiteTable from '@/components/SiteTable.vue';
import AnalyticsChart from '@/components/AnalyticsCharts.vue';
import FilterForm from '@/components/FilterForm.vue';
import SiteDetailModal from '@/components/SiteDetailModal.vue';
import AnalysisForm from '@/components/AnalysisForm.vue';
import ExportButton from '@/components/ExportButton.vue';

// --- State ---
const allSites = ref([]);
const stats = ref({});
const isLoading = ref(true);
const errorMessage = ref('');

// --- Modal State ---
const selectedSiteId = ref(null);
const selectedSiteDetails = ref(null);
const isModalLoading = ref(false);
const showModal = ref(false);

// Filter state
const filters = reactive({
  minScore: 0,
  maxScore: 100,
});

// --- Computed Properties ---
const kpiData = computed(() => {
  if (!stats.value || stats.value.total_sites === 0) return [
    { title: 'Total Sites Analyzed', value: 0 },
    { title: 'Average Score', value: 'N/A' },
    { title: 'Top Site Score', value: 'N/A' },
  ];
  return [
    { title: 'Total Sites Analyzed', value: stats.value.total_sites || 0 },
    { title: 'Average Score', value: stats.value.avg_score ? stats.value.avg_score.toFixed(1) : 'N/A', unit: '/ 100' },
    { title: 'Top Site Score', value: stats.value.max_score || 'N/A', unit: '/ 100' },
  ];
});

const filteredSites = computed(() => {
  return allSites.value.filter(site => {
    const score = site.total_suitability_score || 0;
    return score >= filters.minScore && score <= filters.maxScore;
  });
});

const topTenSites = computed(() => {
  return [...filteredSites.value]
    .sort((a, b) => (b.total_suitability_score || 0) - (a.total_suitability_score || 0))
    .slice(0, 10);
});

// --- Methods ---
async function fetchData() {
  isLoading.value = true;
  errorMessage.value = '';
  try {
    const sitesResponse = await fetch('/api/sites?limit=1000');
    if (!sitesResponse.ok) throw new Error('Failed to fetch sites');
    allSites.value = await sitesResponse.json();

    const statsResponse = await fetch('/api/statistics');
    if (!statsResponse.ok) throw new Error('Failed to fetch statistics');
    stats.value = await statsResponse.json();

  } catch (error) {
    console.error("Error fetching data:", error);
    errorMessage.value = `Failed to load data: ${error.message}. Is the backend server running?`;
  } finally {
    isLoading.value = false;
  }
}

async function handleSiteSelection(siteId) {
  selectedSiteId.value = siteId;
  isModalLoading.value = true;
  showModal.value = true;
  selectedSiteDetails.value = null;

  try {
    const response = await fetch(`/api/sites/${siteId}`);
    if (!response.ok) throw new Error('Failed to fetch site details');
    selectedSiteDetails.value = await response.json();
  } catch (error) {
    console.error(error);
    errorMessage.value = `Error: ${error.message}`;
    closeModal();
  } finally {
    isModalLoading.value = false;
  }
}

function closeModal() {
  showModal.value = false;
  selectedSiteId.value = null;
  selectedSiteDetails.value = null;
}

function handleFilterChange(newFilters) {
  filters.minScore = newFilters.minScore;
  filters.maxScore = newFilters.maxScore;
}

function handleAnalysisComplete() {
  fetchData();
}

// --- Lifecycle Hook ---
onMounted(() => {
  fetchData();
});
</script>

<template>
  <div class="dashboard-container">
    <header>
      <h1>Solar Panel Site Analyzer</h1>
    </header>

    <div v-if="isLoading && allSites.length === 0" class="loading-overlay">
      <div class="spinner"></div>
      <p>Loading site data...</p>
    </div>

    <div v-if="errorMessage" class="error-message">
      {{ errorMessage }}
    </div>

    <template v-if="!isLoading || allSites.length > 0">
      <!-- 1. KPI Section -->
      <section class="kpi-grid">
        <KPICard
          v-for="kpi in kpiData"
          :key="kpi.title"
          :title="kpi.title"
          :value="kpi.value"
          :unit="kpi.unit"
        />
      </section>

      <!-- 2. Analysis & Filter Section -->
      <div class="forms-grid">
        <AnalysisForm @analysis-complete="handleAnalysisComplete" />
        <FilterForm @filter-change="handleFilterChange" />
      </div>

      <!-- 3. Main Content (Map + Analytics) -->
      <section class="main-content-grid">
        <div class="card map-card">
          <h2>Site Map (Showing {{ filteredSites.length }} sites)</h2>
          <SiteMap
            :sites="filteredSites"
            :selected-site-id="selectedSiteId"
            @site-selected="handleSiteSelection"
          />
        </div>

        <div class="card chart-card">
          <h2>Site Score Distribution</h2>
          <AnalyticsChart :sites="filteredSites" />
        </div>
      </section>

      <!-- 4. Top 10 Sites Table -->
      <section class="card table-card">
        <div class="table-header">
          <h2>Top 10 Recommended Sites (from filtered results)</h2>
          <ExportButton :filters="filters" />
        </div>
        <SiteTable
          :sites="topTenSites"
          :selected-site-id="selectedSiteId"
          @site-selected="handleSiteSelection"
        />
      </section>
    </template>
    
    <!-- 5. Site Detail Modal -->
    <SiteDetailModal
      :show="showModal"
      :site="selectedSiteDetails"
      @close="closeModal"
    />
    
  </div>
</template>

<style scoped>
.dashboard-container {
  padding: 1rem; /* Reduced padding for mobile */
}

header h1 {
  margin-bottom: 1.5rem;
  color: #2c3e50;
  font-size: 1.8rem; /* Slightly smaller for mobile */
}

.kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-bottom: 1rem;
}

.forms-grid {
  display: grid;
  grid-template-columns: 1fr; /* Stack forms by default for mobile */
  gap: 1rem;
  margin-bottom: 1rem;
}

.main-content-grid {
  display: grid;
  grid-template-columns: 1fr; /* Stack map/chart by default for mobile */
  gap: 1rem;
  margin-bottom: 1rem;
}

.card {
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  padding: 1.25rem;
  overflow: hidden;
}

.map-card, .chart-card {
  height: 400px; /* Smaller height for mobile */
  display: flex;
  flex-direction: column;
}

.map-card h2, .chart-card h2, .table-card h2 {
  margin-top: 0;
  margin-bottom: 1rem;
  color: #555;
  font-size: 1.1rem;
  font-weight: 600;
}

.table-header {
  display: flex;
  flex-direction: column; /* Stack header on mobile */
  align-items: flex-start;
  gap: 0.5rem;
}
.table-header h2 {
  margin-bottom: 0.5rem;
}

/* --- RESPONSIVE BREAKPOINTS --- */

/* Tablet (and up) */
@media (min-width: 768px) {
  .dashboard-container {
    padding: 2rem;
  }
  header h1 {
    font-size: 2rem;
  }
  .table-header {
    flex-direction: row; /* Un-stack header */
    justify-content: space-between;
    align-items: center;
  }
  .main-content-grid {
    grid-template-columns: 1fr 1fr; /* Map and chart side-by-side */
    gap: 1.5rem;
    margin-bottom: 1.5rem;
  }
  .map-card, .chart-card {
    height: 500px; /* Taller height for desktop */
  }
}

/* Large Desktop */
@media (min-width: 1200px) {
  .forms-grid {
    grid-template-columns: 3fr 2fr; /* Forms side-by-side */
    gap: 1.5rem;
    margin-bottom: 1.5rem;
  }
}


/* Loading/Error States */
.loading-overlay {
  text-align: center;
  padding: 4rem;
}
.spinner {
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 0 auto 1rem;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.error-message {
  padding: 1.5rem;
  background-color: #fbebee;
  color: #c0392b;
  border: 1px solid #c0392b;
  border-radius: 8px;
  margin-bottom: 1rem;
}
</style>