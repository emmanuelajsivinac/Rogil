<template>
    <div v-if="isMenuLoaded" class="menu">
        <!-- Aquí el contenido del menú -->
        <div class="menu-header">
            <img src="./../../public/logos/rogil-logo.jpg" class="img-header" alt="Logo-rogil"/>
        </div>
        <div class="line-h"></div>
        <div class="menu-options">
            <div v-for="(item, index) in parentsMenuOptions" :key="index" class="options">
                <button class="option-value"  @click="handleClick(item.name)">{{ item.name }}</button>
            </div>
        </div>
        <div class="menu-user-options">
            <div class="user-image">
                <img v-if="userPictureURL" :src="userPictureURL" alt="user-picture" width="30" height="30"/>
            </div>
            <div class="user-info">
                <strong>{{ username }}</strong>
                <p>{{ userrole }}</p>
            </div>
            <div class="user-options">
                <img src="./../../public/icons/angulo-derecho.png" alt="user-options" class="user-options-icon"/>
            </div>
        </div>
    </div>
    <div v-else>
        <!-- Un pequeño componente de carga o texto mientras los datos están cargando -->
        <p>Loading menu...</p>
    </div>
</template>



<script>
export default {
    name: 'DashboardMenu',

    data() {
        return {
            parentsMenuOptions: [],
            childsMenuOptions:[],
            username: '',
            userrole: '',
            usercode: '',
            userPictureURL: '',
            menuInfo: '',
            isMenuLoaded: false, // Nueva propiedad para verificar si el menú ya fue cargado
        };
    },

    methods: {
        async getOptionsMenu() {
            try {
                const response = await fetch(`http://192.168.0.7:9090/loadMenu/${this.usercode}`);
                if (response.ok) {
                    const data = await response.json();
                    this.menuInfo = data.menus;
                    console.log(this.menuInfo);


                    this.menuInfo.forEach(parentOption => {
                        if (parentOption.parent === null) {
                            const parentMenuOptions = this.capitalizeShortWord(parentOption.name || '');
                            this.parentsMenuOptions.push({
                                name: parentMenuOptions,
                            });
                        }
                    });

                    this.isMenuLoaded = true; // Indicamos que el menú ya fue cargado
                }

            } catch (error) {
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
            this.username = localStorage.getItem('username') || '';
            this.usercode = localStorage.getItem('usercode') || '';
            this.userrole = localStorage.getItem('userrole') || '';
            console.log("Credentials loaded:", this.username, this.usercode, this.userrole);
        },

        capitalizeShortWord(textvalue) {
            if (typeof textvalue === 'string' && textvalue.length > 0) {
                return textvalue.charAt(0).toUpperCase() + textvalue.slice(1).toLowerCase();
            }
            return textvalue; // Si no es una cadena, devuelve el valor original
        },


        capitalizeLargeWord(textvalue) {
            if (typeof textvalue === 'string' && textvalue.length > 0) {
                return textvalue
                .split(' ')
                .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
                .join(' ');
            }
            return textvalue; // Si no es un string, devuelve el valor original
        },

        getChildOptionMenu(parentMenu){
            localStorage.setItem('childOptionMenu', '');

            this.childsMenuOptions = [];
            console.log(parentMenu);
            parentMenu = parentMenu.toUpperCase();
            console.log("first object",this.menuInfo);

            this.menuInfo.forEach(option => {
                if (option.name === parentMenu) {
                    const parentCode = option.code;
                    const childOptions = this.menuInfo
                        .filter(child => child.parent === parentCode) 
                        .sort((a, b) => a.order - b.order);

                    childOptions.forEach(child => {
                        const childOption = this.capitalizeLargeWord(child.name || '');
                        this.childsMenuOptions.push({
                            name: childOption,
                            route: child.route,
                        });
                    });
                }

            });

            localStorage.setItem('childOptionMenu', JSON.stringify(this.childsMenuOptions));
            console.log(localStorage.getItem('childOptionMenu'))
        },  
        
        handleClick(parentMenu) {
            this.getChildOptionMenu(parentMenu); // Función existente para manejar la lógica de submenús
            this.$emit('show-submenus');// Emite el evento para mostrar SubMenusSection en el componente padre
        }

    },

    mounted() {
        this.loadCredentials();
        if (this.usercode) {
            this.getOptionsMenu();
            this.getUserPicture();
        }
    }
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
    color: #000;
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
}


.option-value{
    font-size: large;
    background-color:  #fff;
    color: #000;
    height: 100%;
    width: 100%;
    transition: background-color 0.1s;
    border-radius: 4px;
}

.option-value:hover{
    background-color: #023535;
    color: #fff;
}

.option-value:active{
    background-color: #015958;
    color: #fff;
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

button{
    margin: 0;
    padding: 0;
    background-color: transparent;
    border: none;
}

button:hover{
    background-color: none;
    color: #fff;
}

button:active{
    background-color: #015958;
    color: #fff;
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