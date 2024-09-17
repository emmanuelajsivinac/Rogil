<template>
  <div class="login-container">
    <form @submit.prevent="loginProcess">
      <div class="login-header">
        <h1>Welcome!</h1> 
        <h5>We are ready to manage the inventory.</h5>    
      </div>
      <div class="login-body">
        <label for="username-entry">User</label>
        <input id="username-entry" v-model="username" required />
        <label for="password-entry">Password</label>
        <input id="password-entry" v-model="password" type="password" required />
      </div>
      <div class="login-button">
        <button type="submit">Sign In</button>
      </div>
    </form>
  </div>
</template>

<script>
export default{
  data(){
    return{
      username: '',
      password: ''
    };
  },
  methods:{
    loginProcess(){
      console.log(this.username);
      console.log(this.password);
    }
  }
}
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

button{
  background: #244E73;
  color: #fff;
  border: none;
  border-radius: 4px;
  width: 100%;
  margin-top: 20px;
  height: 40px;
}
</style>
