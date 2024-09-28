<template>
  <div class="main-container">
    <div class="login-container">
        <div class="login-container-header">
          <img src="./../../public/logos/logo-v1.png" alt="Logo-rogil" class="logo-login"/>
        </div>
        <form class="login-form-container" @submit.prevent="loginProcess">
          <div class="login-header">
            <h1>Welcome!</h1> 
            <h5>We are ready to manage the inventory.</h5>    
          </div>
          <div class="login-body">
            <input id="username-entry" placeholder="Username" v-model="email" required />
            <input id="password-entry" placeholder="Password" v-model="password" type="password" required />
            <div class="options-section">
              <label class="checkbox-keep-log">
                <input type="checkbox">
                Keep me logged in
              </label>
              <label>Forgot password?</label>
            </div>
          </div>
          <div class="login-button">
            <button type="submit">Sign In</button>
          </div>
        </form>
        <div class="login-container-footer">
          <p>© 2024 Rights Reserved</p>
        </div>
    </div>
    <div class="image-container">

    </div>
  </div>
</template>
  
<script>
  export default {
      data() {
        return {
          email: '',
          password: '',
          errorMessage: ''
        };
      },
      methods: {
        async loginProcess() {
          console.log('Intentando iniciar sesión con:', this.email, this.password);

          try {
            const response = await fetch('https://reqres.in/api/login', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                email: this.email,
                password: this.password
              })
            });

            if (response.ok) {
              const data = await response.json();
              console.log('Respuesta recibida:', data); // Verifica los datos

              // Guarda el token en localStorage
              localStorage.setItem('token', data.token); 
              localStorage.setItem('email', this.email);

              console.log(localStorage); // Para ver todos los valores guardados

              // Redirige al dashboard
              this.$router.push('/dashboard');
            } else {
              const errorData = await response.json();
              console.error('Error en la respuesta:', errorData); // Verifica el error
              this.errorMessage = errorData.error || 'Error al iniciar sesión';
            }
          } catch (error) {
            console.error('Error de conexión:', error);
            this.errorMessage = 'Lo sentimos, por favor intente más tarde';
          }
        },

        loadCredentials() {
          this.email = localStorage.getItem('email') || '';
        }

      }

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
    background-color: #F2F2F2;
    background-size: cover;
  }

  .login-container {
    height: 100vh; 
    width: 50vw; 
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    background-color: #F2F2F2;
    border-radius: 8px; 
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }

  .login-container-header{
    height: 8%;
    width: 50vw;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    padding-left: 30px;
    color: #F2F2F2;
    font-size: medium;
  }

  .logo-login{
    height: 40%;
    width: auto;
  }

  .login-form-container{
    height: 60vh;
    width: 25vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .login-header {
    text-align: center;
    margin-bottom: 40px;
    color:#01402E;
  }
  
  h1{
    padding: 0px;
    margin: 0px;
  }
  
  h5{
    padding: 0px;
    margin: 0px;
    font-weight: 500;
  }
  
  .login-body {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  
  input {
    height: 3vw;
    box-sizing:border-box;
    padding: 10px;
    border: 1px solid #3d590223;
    border-radius: 8px;
    background-color: #F2F2F2;
    color: #01402E;
    font-weight: 500;
  }

  input:focus{
    outline: none;
    border: 1px solid #045a5a;
  }

  .options-section{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    font-size: small;
    font-weight: 500;
    color:#015958;  
  }  

  .checkbox-keep-log{
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    font-size: small;
  }
  
  input[type="checkbox"] {
    appearance: none;
    width: 10px;
    height: 10px;
    margin-right: 10px;
    border: 1px solid #0FC2C0;
    border-radius: 4px;
    background-color: #F2F2F2;
    position: relative; /* Añade position relative para el posicionamiento del after */
  }

  input[type="checkbox"]:checked {
    background-color: #0FC2C0; /* Fondo al seleccionar */
    border-color: #0FC2C0; /* Borde del mismo color que el fondo */
  }

  input[type="checkbox"]:checked::after {
    content: '\2714'; /* Símbolo de check */
    color: white;
    font-size: 12px;
    font-weight: bold;
    position: absolute;
    top: 50%; /* Posiciona en el medio verticalmente */
    left: 50%; /* Posiciona en el medio horizontalmente */
    transform: translate(-50%, -50%); /* Ajuste para centrar completamente */
  }


  .login-button{
    width: 100%;
  }

  button{
    width: inherit;
    height: 3vw;
    background: #01402E;
    color: #F2F2F2;
    border: none;
    border-radius: 4px;
    margin-top: 20px;
    font-weight: 500;
    font-size: medium;
  }

  button:hover{
    background: #038C65;
    color: #F2F2F2;
  }

  .login-container-footer{
    height: 8%;
    width: 50vw;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-left: 30px;
    color: #015958;
    font-size: smaller;
    font-weight: 500;
  }

  .image-container {
    height: 100vh; 
    width: 50vw;
    background-image: url("../../public/images/background-login.jpg");
    background-size: cover;
    background-position: center; 
  }

</style>
  
