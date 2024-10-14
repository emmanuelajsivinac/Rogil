<template>
    <div class="dsh-home-main-container">
        <div class="header-section">
            <strong>
                Rebajas y Liquidaciones
            </strong>
        </div>
        <div class="products">
            <p></p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'DashboardHome',

    methods:{
        async getUsers(){
            console.log("ejecutandose getusers")
            try{
                const response = await fetch('http://192.168.0.7:9090/users');
                if (response.ok){
                    console.log("recibiendo respuesta", response.status)
                    const data = await response.text()
                    console.log(data);
                }else{
                    console.log(`Error en la peticion ${response.status}`)
                }

            }catch(error){
                console.log(error);
            }
        },
    }
}

</script>

<style scoped>
.dsh-home-main-container{
    height: 30%;
    width: 100%;
    padding-right: 30px;
    padding-left: 30px;
    display: flex;
    flex-direction: column;
}
</style>