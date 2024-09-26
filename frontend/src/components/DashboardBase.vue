<template>
    <div class="background-container">
        <div class="menu-section">
            <DashboardMenu />
        </div>
        <div class="line-h">
        </div>
        <div class="dashboard-section">
            <div class="dashboard-searchsection">
                <DashboardSearchSection />
            </div>
            <div class="line-v">
            </div>
            <div class="dashboard">
            </div>
        </div>
    </div>
</template>

<script>
import DashboardMenu from './DashboardMenu.vue';
import DashboardSearchSection from './DashboardSearchSection.vue';

export default {
  name: 'DashboardBase',
  components:{
    DashboardMenu,
    DashboardSearchSection
  },
};
</script>

<style scoped>
.background-container{
    height: 100vh;
    width: 100vw;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: row;
}

.menu-section {
    height: 100vh;
    width: 20vw;
    background-color: #EBF1F2;
}

.line-h{
    height: 100vh;
    width: 0.05%;
    background-color: #d1d6d7;
}

.dashboard-section{
    height: 100vh;
    width: 80vw;
    display: flex;
    flex-direction: column;
    background-color: #EBF1F2;
}

.dashboard-searchsection{
    height: 10vh;
    width: 100%;
    background-color: #EBF1F2;
}

.line-v{
    height: 0.1%;
    width: 100vw;
    background-color: #d1d6d7;
}
</style>