<template>
    <v-app>
        <v-main v-if="!test">
            <c-menu></c-menu>
            <router-view />
        </v-main>
        <v-main v-else>
          <c-header></c-header>
        </v-main>
    </v-app>
</template>

<script>
import store from './store'
import CMenu from './components/c-menu.vue'
import CHeader from './components/c-header.vue'
export default {
  name: 'App',
  components: {
    'c-menu': CMenu,
    'c-header': CHeader
  },
  data () {
    return {
        logged: store.state.authonticated,
        test: false
    }
  },
  created() {
    this.$watch('$route.path', () => {
      if (!this.$cookies.isKey('opt-token')) {
        this.$router.push('/auth')
      }
      if (this.$route.path === '/customers') {
        this.test = true;
      } else {
        this.test = false
      }
    })
  },
}
</script>
