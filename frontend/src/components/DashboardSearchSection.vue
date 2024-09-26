<template>
    <div class="search-section">
        <div class="section-A">
            <h1>Welcome {{ email }} !</h1>
        </div>
        <div class="section-B">
            <div class="search">
                <img src="./icons/busqueda.png">
            </div>
            <div class="user">
                <div class="user-info">
                    <p>{{ email }} </p>
                    <p>Admin</p> 
                </div>
                <div class="user-option">
                    <select>
                        <option value="" disabled selected hidden></option>
                        <option>Settings</option>
                        <option>Sign out</option>
                    </select>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DashboardSearchSection',
    data() {
        return {
        email: ''
        };
    },

    created() {
        console.log('Componente creado');
        this.loadCredentials();
    },
            
    methods: {
        loadCredentials() {
        this.email = localStorage.getItem('email') || '';
        console.log('Email cargado:', this.email); 
        }
    }
};
</script>

<style scoped>
.search-section{
    box-sizing:border-box;
    height: 100%;
    width: 100%;
    padding-left: 30px;
    padding-right: 30px;
    margin: 0;
    display: flex;
    align-items: center; 
    justify-content: space-between;
} 

.section-A{
    height: 100%;
    width: 65%;
    font-size: small;
}

.section-B{
    height: 100%;
    width: 35%;
    font-size: small;
    display: flex;
    align-items: center;  
}

.search{
    height: 100%;
    width: 50%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

img{
    height: 40%;
    width: auto;

}

.user{
    height: 100%;
    width: 50%;
    margin: 0;
    padding: 0;
    display: flex;
    justify-items: center;
    align-items: center;
}

.user-info{
    margin: 0;
    padding: 0;
    width: 90%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

p{
    margin: 0;
    padding: 0;
}

.user-option{
    margin: 0;
    padding: 0;
    width: 10%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

select {
    appearance: none;
    width: 30px; /* Ajusta el ancho */
    height: 100%;
    border: none;
    background: url("./icons/menu-puntos-vertical.png") no-repeat center right;
    background-size: 20px;
    padding-right: 20px;
    cursor: pointer;
    position: relative;
}

select option {
    text-align: left;
    padding-left: 10px;
}

select option[disabled] {
    display: none;
}

select option {
    position: relative;
    left: -20px;
}
</style>