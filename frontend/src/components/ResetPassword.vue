<template>
    <div class="main-container">
      <div class="reset-container">
          <div class="reset-container-header">
            <img src="./../../public/logos/rogil-logo.jpg" alt="Logo-rogil" class="logo-reset"/>
          </div>
          <form class="reset-form-container" @submit.prevent="loginProcess">
            <div class="reset-header">
              <strong>Reset your Password</strong> 
              <p>To reset your password, you need an administrator user to complete this request.</p>    
            </div>
            <div class="reset-body">
              <div class="aminuser-section">
                <p>Administrator user</p>
                <input id="username-entry" placeholder="Username" v-model="email" required />
                <input id="password-entry" placeholder="Password" v-model="password" type="password" required />
              </div>
              <div class="newpassword-section">
                <p>Password</p>
                <input id="new-password" placeholder="New password" v-model="newpassword" required />
                <input id="confirm-password" placeholder="Confirm password" v-model="confirmpassword" required />
              </div>
            </div>
            <div class="reset-button">
              <button type="submit">Submit</button>
            </div>
          </form>
          <div class="reset-container-footer">
            <p>© 2024 Rights Reserved</p>
          </div>
      </div>
    </div>
  </template>
    
  <script>
    export default {
        name: 'ResetPassword'
    }
  
  </script>
    
  <style scoped>
    .main-container{
      box-sizing:content-box;
      margin: 0;
      padding: 0;
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction:row;
      align-items: center;
      justify-content: center;
      background-color: #FFF;
      background-size: cover;
    }
  
    .reset-container {
      height: 100vh; 
      width: 100vw; 
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
      background-color: #FFF;
    }
  
    .reset-container-header{
      height: 8%;
      width: 100vw;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding-left: 30px;
      color: #FFF;
      font-size: medium;
    }
  
    .logo-reset{
      height: 40%;
      width: auto;
    }
  
    .reset-form-container{
      height: 65vh;
      width: 25vw;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-between;
    }
  
    .reset-header {
      text-align: center;
      color: #023535;
      margin-bottom: 20px;
    }
    
    strong{
      padding: 0px;
      margin: 0px;
      font-size: xx-large;
    }
    
    p{
      padding: 0px;
      margin: 0px;
      font-weight: 500;
    }
    
    .reset-body {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 10px;
      color: #023535;
    }

    .aminuser-section{
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    
    input {
      height: 3vw;
      box-sizing:border-box;
      margin-top: 10px;
      padding: 15px;
      border: 1px solid #AFB09D;
      border-radius: 8px;
      background-color: #FFF;
      color: #015958;
      font-weight: 500;
      font-size: medium;
    }
  
    input:focus{
      outline: none;
      border: 1px solid #045a5a;
    }
  
    .newpassword-section{
      width: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }  
  
    .checkbox-keep-log{
      margin: 0;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      font-size: small;
      height: 30px;
    }
  
    input[type="checkbox"]{
      margin-right: 10px;
    }
  
    
  
    .reset-button{
      width: 100%;
    }
  
    button{
      width: inherit;
      height: 3vw;
      background: #023535;
      color: #FFF;
      border: none;
      border-radius: 4px;
      margin-top: 20px;
      font-weight: 500;
      font-size: medium;
    }
  
    button:hover{
      background: #015958;
      color: #FFF;
    }
  
    .reset-container-footer{
      height: 8%;
      width: 100vw;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      justify-content: center;
      padding-left: 30px;
      color: #818274;
      font-size: smaller;
      font-weight: 500;
    }
  
  </style>
    
  