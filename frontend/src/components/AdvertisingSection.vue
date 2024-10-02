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
      // Lista de imágenes para alternar
      images: [
        '../../public/Post/431941784_825795049581419_7459982851608864249_n.jpeg',
        '../../public/Post/98204202_593384551282078_8333200263296843776_n.jpg',
        '../../public/Post/442409517_860002932827297_8134513836530527603_n.png',
        '../../public/Post/277249040_996736460946883_6903668697496611952_n.png',

      ],
      currentIndex: 0, // Índice para controlar la imagen actual
      currentImage: '' // Variable que contiene la URL de la imagen actual
    };
  },
  mounted() {
    // Iniciamos con la primera imagen
    this.currentImage = this.images[this.currentIndex];

    // Cambiar la imagen cada 10 segundos
    setInterval(() => {
      this.currentIndex = (this.currentIndex + 1) % this.images.length; // Alternar el índice
      this.currentImage = this.images[this.currentIndex]; // Actualizar la imagen
    }, 2500); // 10000 milisegundos = 10 segundos
  }
};
</script>


<style scoped>
.ad-main-container {
    height: 40vh;
  box-sizing: border-box;
  padding:30px;
}

.ad-images-section {
  padding-left: 30px;
  padding-right: 30px;
  border-radius: 4px;
  display: flex;
  justify-content: center;
  height: 100%;
  width: 100%; /* Ajusta la altura del contenedor principal */
  overflow: hidden; /* Oculta cualquier desbordamiento */
}

.post-images {
  height: auto;
  width: 100%; /* La imagen se ajusta a la altura del contenedor */
  object-fit: contain; /* Mantiene la proporción de la imagen y la ajusta */
  border-radius: 4px;
}

</style>