import { createStore } from 'vuex';

const store = createStore({
  state: {
    email: null,
  },
  mutations: {
    setUser(state, email) {
      state.email = email;
    },
  },
  actions: {
    // Puedes agregar acciones para manejar lógica asíncrona si lo necesitas
  },
  getters: {
    isAuthenticated: state => !!state.email,
    getUser: state => state.email,
  }
});

export default store;
