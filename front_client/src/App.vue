<template>
  <div id="app">
    <c-menu />
    <div class="container">
          <router-view/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

import CMenu from './components/c-menu'

export default {
  name: 'App',
  components: {
    CMenu
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
