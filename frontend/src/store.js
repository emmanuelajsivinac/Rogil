import { createStore } from 'vuex';

const store = createStore({
  state: {
    email: null,
    username: null,
    usercode: null,
    childMenuOptions: [], // Cambiado a childMenuOptions
  },
  mutations: {
    setUser(state, { email, username, usercode }) {
      state.email = email;
      state.username = username;
      state.usercode = usercode;
    },
    setChildMenuOptions(state, options) { // Cambiado a setChildMenuOptions
      state.childMenuOptions = options; // Mutación para actualizar las opciones de menú secundarias
      localStorage.setItem('childOptionMenu', JSON.stringify(options)); // Sincroniza con localStorage
    },
    loadChildMenuOptionsFromStorage(state) { // Cambiado a loadChildMenuOptionsFromStorage
      const menuOptions = localStorage.getItem('childOptionMenu');
      if (menuOptions) {
        state.childMenuOptions = JSON.parse(menuOptions); // Carga desde localStorage
      }
    },
  },
  actions: {
    loadChildMenuOptions({ commit }) { // Cambiado a loadChildMenuOptions
      commit('loadChildMenuOptionsFromStorage'); // Acción para cargar opciones
    },
  },
  getters: {
    isAuthenticated: (state) => !!state.email,
    getUser: (state) => state.email,
    getChildMenuOptions: (state) => state.childMenuOptions, // Getter para obtener opciones de menú secundarias
  },
});

export default store;
