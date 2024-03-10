<template>
    <v-app class="container">
      <v-main>
        <div v-if="test">
          <c-menu></c-menu>
          <router-view />
        </div>
        <div v-else>
          <c-auth />
        </div>
      </v-main>
    </v-app>
</template>

<script>
import store from './store'
import CMenu from './components/c-menu.vue'
import CHeader from './components/c-header.vue'
import CAuth from './views/Auth/Auth'
export default {
  name: 'App',
  components: {
    'c-menu': CMenu,
    'c-header': CHeader,
    'c-auth': CAuth
  },
  data () {
    return {
        logged: store.state.authonticated,
        test: this.$cookies.isKey('opt-token')
    }
  }
}
</script>
