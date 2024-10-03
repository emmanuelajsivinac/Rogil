<template>
    <div class="ad-main-container">
        <div class="ad-images-section">
            <img :src="currentImage" class="post-images">
        </div>
    </div>
</template>

<script>
export default {
  name: 'AdvertisingSection',
  data() {
    return {
            images: [
            '../../public/Post/431941784_825795049581419_7459982851608864249_n.jpeg',
            '../../public/Post/442409517_860002932827297_8134513836530527603_n.png',
            '../../public/Post/277249040_996736460946883_6903668697496611952_n.png',
      ],
      currentIndex: 0, 
      currentImage: ''
    };
  },
  mounted() {
    this.currentImage = this.images[this.currentIndex];

    setInterval(() => {
      this.currentIndex = (this.currentIndex + 1) % this.images.length; 
      this.currentImage = this.images[this.currentIndex];
    }, 2500);
  }
};
</script>


<style scoped>
.ad-main-container {
    height: 40vh;
  box-sizing: border-box;
  padding:30px;
  display: flex;
  align-items: center;
  justify-content: center
}

.ad-images-section {
  box-sizing: border-box;
  padding-left: 30px;
  padding-right: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 58%; /* Ajusta la altura del contenedor principal */
  overflow: hidden; /* Oculta cualquier desbordamiento */
  background-color: #dfdfdf;
  border-radius: 4px
}

.post-images {
  
  height: 100%;
  width: auto; /* La imagen se ajusta a la altura del contenedor */
  object-fit: contain; /* Mantiene la proporción de la imagen y la ajusta */
  border-radius: 4px;
}

</style>