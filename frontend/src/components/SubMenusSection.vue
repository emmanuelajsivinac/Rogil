<template>
    <div class="main-container">
      <div v-for="(item, index) in childs" :key="index" class="options">
        <button class="option-value" @click="getRoute(index, item.route)">{{ item.name }}</button> <!-- Ahora item tiene una propiedad 'name' -->
      </div>
    </div>
  </template>
      
<script>  
  export default {
    name: 'SubMenusSection',
    route: '',
  
    data() {
      return {
        childMenuOptions: [],  // Array que contendrá las opciones del submenú
        lastChildOptionMenu: '', // Almacena la última versión de childOptionMenu en localStorage
        childs: [], // Será el array que usarás en el v-for
      };
    },
  
    mounted() {
      // Ejecutar la verificación en intervalos regulares
      this.intervalId = setInterval(() => {
        this.checkStorageChange();
      }, 50); // Ajustado a 1 segundo (1000 ms) para no sobrecargar la aplicación
    },
  
    beforeUnmount() {
      // Limpiar el intervalo al desmontar el componente
      clearInterval(this.intervalId);
    },
  
    methods: {
      loadChildMenuOptions() {
        // Recuperar los datos del localStorage
        const childOptions = localStorage.getItem('childOptionMenu');
        console.log('Loaded Sub Menu Options:', childOptions);
  
        if (childOptions) {
          this.childMenuOptions = JSON.parse(childOptions); // Parsear y guardar el array de objetos
          this.childs = this.childMenuOptions; // Asignar el array completo a childs
        } else {
          this.childs = []; // Si no hay datos, asegurarse de que childs esté vacío
        }
      },
  
      checkStorageChange() {
        // Verificar si los datos en localStorage han cambiado
        const currentMenu = localStorage.getItem('childOptionMenu');
        if (currentMenu !== this.lastChildOptionMenu) {
          this.lastChildOptionMenu = currentMenu; // Actualizar la última versión
          console.log('Los datos en localStorage han cambiado.');
          this.loadChildMenuOptions(); // Cargar las nuevas opciones si hay un cambio
        }
      },

      getRoute(index, route){
        this.route = route;
        console.log(this.route);
        console.log(index);
      }
    }
  };
</script>
  
<style scoped>
.main-container{
  display: flex;
  flex-direction: column;
  align-items: center;
} 
.options{
  box-sizing: border-box;
    width: 95%;
    height: 30%;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    margin: 0;
    padding: 0;
}

.option-value{
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  background-color: #023535;
  color: #fff;
  font-weight: 500;
  border: none;
  border-radius: 4px;
}

.option-value:hover{
    background-color: #015958;
    color: #fff;
}

.option-value:active{
    background-color: #015958;
    color: #fff;
}

</style>

  