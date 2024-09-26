<template>
    <div class="menu">
        <div class="menu-header">
            <img src="./../../public/logos/logo-v1.png" alt="Logo-rogil" class="logo-menu"/>
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
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center; 
    justify-content: center;
    background-color: #EBF1F2;
}    

.menu-header{
    width: 100%;
    height: 10vh;
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center; 
    justify-content: center;
}

.logo-menu{
    height: 40%;
    width: auto;
}
</style>