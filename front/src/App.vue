<template>
    <v-app>
        <v-main>
            <c-menu></c-menu>
            <router-view />
        </v-main>
    </v-app>
</template>

<script>

import CMenu from './components/c-menu.vue'
export default {
  name: 'App',
  components: {
    'c-menu': CMenu
  },
  data () {
    return {
    }
  },
  created() {
    this.$watch('$route.path', () => {
      if (!this.$cookies.isKey('opt-token')) {
        this.$router.push('/auth')
      }
    })
  },
}
</script>
