<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <h1> APP.VUE </h1>
  <router-link to="/hello">Hello</router-link> |
  <router-view/>
</template>

