<template>
  <div class="main-container">
    <UserLogin />
  </div>
</template>

<script>
import UserLogin from './components/UserLogin.vue'

export default {
  name: 'App',
  components: {
    UserLogin
  }
}
</script>

<style>

.main-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

html, body {
  font-family: "SUSE", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
  margin: 0; 
  padding: 0; 
  font-size:larger;
}
</style>
