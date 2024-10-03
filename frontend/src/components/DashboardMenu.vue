<template>
    <div class="menu">
        <div class="menu-header">
            <img src="./../../public/logos/rogil-logo.jpg" class="img-header" alt="Logo-rogil"/>
        </div>
        <div class="line-h"></div>
        <div class="menu-options">
            <div v-for="(item, index) in optionsMenuItems" :key="index" class="options">
                <p class="option-value">{{ item }}</p>
            </div>
        </div>
        <div class="menu-user-options">
            <div class="user-image">
                <img v-if="userPictureURL" :src="userPictureURL" alt="user-picture" width="30" height="30"/>
            </div>
            <div class="user-info">
                <strong>{{ email }}</strong>
                <p>{{ role }}</p>
            </div>
            <div class="user-options">
                <img src="./../../public/icons/angulo-derecho.png" alt="user-options" class="user-options-icon"/>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'DashboardMenu',

    data(){
        return {
            optionsMenuValues : [],
            email: '',
            role: 'Administrator',
            userPictureURL: '',
        };
    },

    methods:{
        async getOptionsMenu(){
            try{
                const response = await fetch('https://dummyjson.com/products/category-list');
                if (response.ok){
                    const data = await response.json()
                    this.optionsMenuValues = Object.values(data);
                }

            }catch(error){
                console.log(error);
            }
        },

        async getUserPicture() {
            try {
                const response = await fetch('https://dummyjson.com/icon/abc123/150');
                if (response.ok) {
                    const picture = await response.blob();
                    this.userPictureURL = URL.createObjectURL(picture);
                }
            } catch (error) {
                console.log(error);
            }
        },



        loadCredentials() {
        this.email = localStorage.getItem('email') || '';
        }
    },

    computed:{
        optionsMenuItems(){
            return this.optionsMenuValues.slice(0,5);
        }
    },

    mounted() {
        this.getOptionsMenu();
        this.getUserPicture();
    },

    created() {
        this.loadCredentials();
    },
}
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
    box-sizing: border-box;
    width: 100%;
    height: 12%;
    margin: 0;
    padding-top: 30px;
    padding-left: 30px;
    padding-right: 30px;
    padding-bottom: 25px;
    display: flex;
    align-items: flex-start; 
    justify-content: flex-start;
}

.img-header{
    height: 100%;
    width: auto;
    padding: 0;
    margin: 0;
}

.line-h{
    height: 0.2%;
    width: 90%;
    background-color: #d1d6d7;
}

.menu-options{
    width: 100%;
    height: 75%;
    margin-top: 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}

.options{
    box-sizing: border-box;
    width: 80%;
    height: 10%;
    text-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 4px;
    transition: background-color 0.1s;
}

.options:hover{
    background-color: #023535;
    color: #fff;
}

.options:active{
    background-color: #015958;
    color: #fff;
}

.option-value{
    font-size: medium;
}

.menu-user-options{
    box-sizing: border-box;
    width: 80%;
    height: 8%;
    padding-left: 10px;
    padding-right: 10px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    border-radius: 4px;
    background-color: #023535;
    color: #fff;
    transition: background-color 0.1s;;  
}

.menu-user-options:hover{
    background-color: #015958;
    color: #fff;
}

.user-image{
    height: 30px;
    width: 30px;
    padding: 0;
    margin: 0;
    background-color: #fff;
    border-radius: 50px
}

.user-info{
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
    justify-content: center;
}

strong{
    margin: 0;
    padding: 0;
    font-size: small;
}

p{
    margin: 0;
    padding: 0;
    font-size: x-small;
}

.user-options{
    height: 30px;
    width: 20px;
    padding: 0;
    margin: 0;
    display: flex;
    align-items: center;
}

.user-options-icon{
    height: 50%;
    width: auto;
}

</style>