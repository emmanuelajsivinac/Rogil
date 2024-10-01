<template>
    <div class="search-section">
        <div class="section-A">
            <div class="greeting-section">
                <strong>{{ greeting }} {{ email }} !</strong>
            </div>
            <div class="date-section">
                <p>{{ formated_date }}</p>
            </div>
        </div>
        <div class="section-B">
            <div class="options-section">
                <div class="search">                
                    <img src="./../../public/icons/busqueda.png">
                </div>
                <div class="line-v"></div>
                <div class="notification">
                    <img src="./../../public/icons/campana.png">
                </div>
                <div class="screen-view">
                    <button>Full screen</button>
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
        greeting: null,
        email: '',
        formated_date: null
        };
    },

    created() {
        this.loadCredentials();
    },

    mounted(){
        const date = new Date();
        const dayList = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
        const monthList = ['January','February','March','April','May','June','July','August','September','October','November','December'];
        const day = dayList[date.getDay()];
        const dayNumber = date.getDate();
        const month = monthList[date.getMonth()];
        this.formated_date = `${day} ${dayNumber}, ${month}`;
        
        const time = date.getHours();
        this.greeting = time < 12 ? 'Good morning' : time>18 ? 'Good night' : 'Good afternoon';
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
    padding:0;
    display: flex;
    align-items: center; 
} 

.section-A{
    height: 100%;
    width: 80%;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    text-align: start;
    justify-content:flex-start;
}

.greeting-section{
    font-size: x-large;
    margin: 0;
    padding: 0;
}

.date-section{
    margin: 0;
    padding: 0;
}

p{
    margin: 0;
    padding: 0;
}

.section-B{
    height: 100%;
    width: 20%;
    padding: 0;
    margin: 0;
    font-size: small;
    display: flex;
    flex-direction: column;
    align-content: center;
    justify-content:flex-start;
}

.options-section{
    margin: 0;
    padding: 0;
    display: flex;
    height: 50%;
    width: 100%;
    display: flex;
    justify-content: center;
    align-content: center;
    align-items: center;
    
}

.search{
    width: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.line-v{
    width: 1px;
    height: 60%;
    background-color: #d1d6d7;
}

.notification{
    width: 20%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.screen-view{
    width: 49%;
    height: 100%;
    padding-left: 5PX;
    display: flex;
    justify-content: center;
    align-items: center;
}

button{
    height: 100%;
    width: 100%;
    border: none;
    border-radius: 4px;
    background-color: #d1d6d7;
    font-size: 90%;
    font-weight:500;
    color: #000;
}

button:hover{
    background-color: #e7edee;
}

img{
    height:20px;
    width: auto;
}

</style>