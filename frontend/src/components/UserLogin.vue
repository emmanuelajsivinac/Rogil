<template>
  <div class="login-container">
    <div class="login-header">
      <h1>Welcome!</h1> 
      <h5>We are ready to manage the inventory.</h5>    
    </div>
    <div class="login-body">
      <label for="username-entry">User</label>
      <input id="username-entry" required />
      <label for="password-entry">Password</label>
      <input id="password-entry" type="password" required />
    </div>
  </div>
</template>

<script>

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  background-color: #fff;
}

.login-header {
  text-align: center;
  margin-bottom: 40px;
}

h1{
  padding: 0px;
  margin: 0px;
}

h5{
  padding: 0px;
  margin: 0px;
  font-weight: 300;
}

.login-body {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

label {
  font-weight: bold;
}

input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
</style>
