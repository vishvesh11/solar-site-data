<script setup>
defineProps({
  sites: Array,
  selectedSiteId: Number
});
const emit = defineEmits(['site-selected']);

function handleRowClick(siteId) {
  emit('site-selected', siteId);
}
</script>

<template>
  <div class="table-wrapper">
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Site Name</th>
          <th>Region</th>
          <th>Area (m²)</th>
          <th>Grid (km)</th>
          <th>Slope (°)</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(site, index) in sites"
          :key="site.site_id"
          @click="handleRowClick(site.site_id)"
          :class="{ 'selected-row': site.site_id === selectedSiteId }"
        >
          <td>{{ index + 1 }}</td>
          <td>{{ site.site_name }}</td>
          <td>{{ site.region }}</td>
          <td>{{ site.area_sqm.toLocaleString() }}</td>
          <td>{{ site.grid_distance_km }}</td>
          <td>{{ site.slope_degrees }}</td>
          <td>
            <strong>{{ site.total_suitability_score?.toFixed(1) || 'N/A' }}</strong>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="!sites || sites.length === 0" class="no-data">
      No sites match the current filter criteria.
    </div>
  </div>
</template>

<style scoped>
.table-wrapper {
  width: 100%;
  overflow-x: auto; 
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}
th, td {
  padding: 0.75rem 1rem;
  text-align: left;
  border-bottom: 1px solid #eee;
  white-space: nowrap;
}
th {
  background-color: #f9f9f9;
  font-weight: 600;
  color: #555;
}
tbody tr {
  cursor: pointer;
  transition: background-color 0.2s ease;
}
tbody tr:hover {
  background-color: #f5f5f5;
}
.selected-row {
  background-color: #e3f2fd; 
}
td strong {
  font-size: 1rem;
  font-weight: 600;
  color: #3498db;
}
.no-data {
  padding: 2rem;
  text-align: center;
  color: #777;
}
</style>