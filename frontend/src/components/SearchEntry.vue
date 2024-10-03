<template>
    <div class="search-main-container">
      <div class="search-entry-elements">
        <img src="./../../public/icons/busqueda.png" alt="Buscar" />
        <input placeholder="Search" v-model="searchValue" />
      </div>
      <div class="result-section">
        <ul>
          <li v-for="item in results" :key="item.id">{{ item.title }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, watch } from 'vue';
  
  export default {
    name: 'SearchEntry',
  
    setup() {
      const searchValue = ref('');
      const results = ref([]); 
  
      const getResultsForEnteredValue = async () => {
        if (searchValue.value.trim() === '') {
          results.value = [];
          return;
        }
  
        try {
          const response = await fetch(`https://dummyjson.com/products/search?q=${searchValue.value}`);
          if (response.ok) {
            const data = await response.json();
            console.log(data);
            results.value = data.products.slice(0, 3);
          } else {
            console.error(`Error en la petición: ${response.status}`);
          }
        } catch (error) {
          console.error('Error en la búsqueda:', error.message);
        }
      };

      watch(searchValue, (newValue) => {
        getResultsForEnteredValue();
      });
  
      return {
        searchValue,
        results, 
      };
    },
  };
  </script>
  
<style scoped>
.search-main-container{
    box-sizing: border-box;
    padding-left: 30px;
    padding-right: 30px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    background-color: #fff;
}

.search-entry-elements{
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}

img{
    height: 25px;
}

input{
    padding: 10px;
    background-color: inherit;
    border: none;
    color: #015958;
    font-size: xx-large;
}

input::placeholder{
    color: #0CABA8;
    font-size: xx-large;
}

input:focus{
   outline: none;
}

.result-section{
    padding-left: 30px;
}

p{
    margin: 0;
}

ul{
    margin: 0;
    padding: 0;
}
li{
    margin: 0; 
    padding: 0;
    list-style-type: none;
}

</style>