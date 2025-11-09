<script setup>

import "leaflet/dist/leaflet.css";


import L from 'leaflet';
import iconUrl from 'leaflet/dist/images/marker-icon.png';
import iconShadowUrl from 'leaflet/dist/images/marker-shadow.png';

import { LMap, LTileLayer, LCircleMarker, LTooltip, LMarker } from "@vue-leaflet/vue-leaflet";
import { ref, computed, watch } from "vue";


const defaultIcon = L.icon({
  iconUrl,
  shadowUrl: iconShadowUrl,
  iconAnchor: [12, 41], 
  shadowAnchor: [12, 41],
  popupAnchor: [1, -34],
  tooltipAnchor: [16, -28],
  iconSize: [25, 41],
  shadowSize: [41, 41]
});

const selectedIcon = defaultIcon; 


const props = defineProps({
  sites: Array,
  selectedSiteId: Number
});

const emit = defineEmits(['site-selected']);


const zoom = ref(6); 
const mapRef = ref(null); 

const center = computed(() => {

  if (props.sites && props.sites.length > 0) {
    return [props.sites[0].latitude, props.sites[0].longitude];
  }
  return [20.5937, 78.9629];
});


function getScoreColor(score) {
  if (score === null || score === undefined) return '#95a5a6'; // grey for null
  if (score >= 80) return '#2ecc71'; // green
  if (score >= 60) return '#f1c40f'; // yello
  if (score >= 40) return '#e67e22'; // orange
  return '#e74c3c'; // red
}

function handleMarkerClick(siteId) {
  emit('site-selected', siteId);
}


watch(() => props.selectedSiteId, (newId) => {
  if (newId === null || !mapRef.value) return;

  const site = props.sites.find(s => s.site_id === newId);
  if (site) {

    mapRef.value.leafletObject.flyTo([site.latitude, site.longitude], 12); 
  }
});
</script>

<template>
  <div style="height:100%; width:100%">
    <LMap ref="mapRef" v-model:zoom="zoom" :center="center">
      <LTileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution="&copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors"
      />
      
      <LCircleMarker
        v-for="site in sites"
        :key="site.site_id"
        :lat-lng="[site.latitude, site.longitude]"
        :radius="site.site_id === selectedSiteId ? 12 : 8"
        :color="getScoreColor(site.total_suitability_score)"
        :fill="true"
        :fill-opacity="0.7"
        :weight="site.site_id === selectedSiteId ? 3 : 1"
        :stroke="true"
        @click="handleMarkerClick(site.site_id)"
      >
        <LTooltip>
          <strong>{{ site.site_name }}</strong><br>
          Score: {{ site.total_suitability_score?.toFixed(1) || 'N/A' }}
        </LTooltip>
      </LCircleMarker>
    </LMap>
  </div>
</template>
