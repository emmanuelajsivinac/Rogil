<template>
    <div class="background-container">
        <div class="menu-section">
            <DashboardMenu />
        </div>
        <div class="line-h">
        </div>
        <div class="dashboard-section">
            <div class="dashboard-searchsection">
                <DashboardSearchSection @showComponent="showComponent" />
            </div>
             <transition name="slide">
                <SearchEntry v-if="showSearchEntry" class="overlay"/>
             </transition>
            <div class="dashboard">
                <AdvertisingSection />
                <DashboardHome />
            </div>
        </div>
    </div>
</template>

<script>
import DashboardMenu from './DashboardMenu.vue';
import DashboardSearchSection from './DashboardSearchSection.vue';
import SearchEntry  from './SearchEntry.vue';
import AdvertisingSection from './AdvertisingSection.vue';
import DashboardHome from './DashboardHome.vue';

export default {
  name: 'DashboardBase',
  components:{
    DashboardMenu,
    DashboardSearchSection,
    SearchEntry,
    AdvertisingSection,
    DashboardHome
  },

  data(){
    return {
        showSearchEntry:false,
    };
  },

  methods: {
    showComponent() {
      this.showSearchEntry = !this.showSearchEntry; // Cambia el estado a verdadero para mostrar el componente
    },
  },
};
</script>


<style scoped>
.background-container {
    height: 100vh;
    width: 100vw;
    display: flex;
    flex-direction: row;
}

.menu-section {
    height: 100vh;
    width: 20vw;
    background-color: #EBF1F2;
}

.line-h {
    height: 100vh;
    width: 0.05%;
    background-color: #d1d6d7;
}

.dashboard-section {
    height: 100vh;
    width: 80vw;
    display: flex;
    flex-direction: column;
    position: relative; /* Para que el contenedor 'SearchEntry' use esta referencia */
    background-color: #fff;
}

.dashboard-searchsection {
    height: 15vh;
    width: 100%;
    padding: 0;
    z-index: 1;
}

.dashboard {
    z-index: 0;
}

.overlay {
    position: absolute;
    top: 15vh;
    left: 0;
    width: 100%;
    height: 25%;
    z-index: 2;
    transition: all 0.5s ease-in-out;
}

/* Estilos de transición */
.slide-enter-active, .slide-leave-active {
    transition: all 0.5s ease;
}
.slide-enter, .slide-leave-to {
    opacity: 0;
    transform: translateY(-20px);
}
</style>