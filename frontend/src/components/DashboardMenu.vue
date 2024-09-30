<template>
    <div class="menu">
        <div class="menu-header">
            <img src="./../../public/logos/rogil-logo.jpg" alt="Logo-rogil"/>
        </div>
        <div class="menu-options">
            <div class="options">
                           </div>
            <div class="options">
   
            </div>
            <div class="options">
  
            </div>
        </div>
        <div class="menu-user-options">

        </div>
    </div>
</template>

<script>
export default {
    name: 'DashboardMenu'
};
</script>

<style scoped>
.menu{
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center; 
    justify-content: flex-start;
    background-color: #fff;
}    

.menu-header{
    width: 100%;
    height: 4%;
    margin: 0;
    padding-top: 20px;
    display: flex;
    align-items: center; 
    justify-content: flex-start;
}

img{
    height: 100%;
    width: auto;
    padding: 0;
    margin-left: 20px;
}

.menu-options{
    width: 100%;
    height: 20%;
    display: flex;
    flex-direction: column;
    justify-items: center;
    align-items: flex-start;
    justify-content: space-between;
    padding: 20px;
}

.options:focus{
    background-color: #008F8C;
}

</style>