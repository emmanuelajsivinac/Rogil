<template>
    <div class="search-main-container">
        <div class="search-entry-elements">
            <img src="./../../public/icons/busqueda.png">
            <input placeholder="Search">
        </div>
        <div class="result-section">
            <p>-> Products</p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SearchEntry'
}
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

</style>