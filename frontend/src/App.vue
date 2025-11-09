<script setup>



import DashboardView from './views/DashboardView.vue' 

console.log('App.vue is running (Bypass Test)');
</script>

<template>
  <main>
    <h1>Hello, this is App.vue</h1> 
    <DashboardView /> 

  </main>
</template>

<style scoped>

main {
  width: 100%;
  min-height: 100vh;
  background-color: #f4f7fa;
}
h1 {
  padding: 1rem 2rem;
  background-color: #34495e;
  color: white;
}
</style>