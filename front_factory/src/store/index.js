import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    authonticated: false
  },
  mutations: {
    setAuth (state, bool) {
      state.authonticated = bool
    }
  },
  actions: {
  },
  modules: {
  }
})
