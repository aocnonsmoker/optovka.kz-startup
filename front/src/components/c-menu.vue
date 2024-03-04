<template>

    <v-navigation-drawer color="light-blue darken-4" app>
      <v-sheet color="grey lighten-4" class="pa-4">
        <div>Название компаний</div>
      </v-sheet>

      <v-divider></v-divider>

      <v-list dense>
        <v-subheader color="blue darken-3" dark>МЕНЮ</v-subheader>
        <v-list-item-group v-model="selectedItem" color="primary" dark>
          <v-list-item v-for="(item, i) in items" :key="i">
            <v-list-item-content>
              <router-link style="color: #ffffff" :to="item.path">
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>

                {{ item.text }}
              </router-link>
              <!-- <v-list-item-title v-text="item.text"> </v-list-item-title> -->
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>

      <template v-slot:append>
   <v-divider

   dark></v-divider>
 <v-list-item dark>
            <v-list-item-action>
           Название пользователя
            </v-list-item-action>

    <v-spacer></v-spacer>

                <v-btn
                v-ripple="false"
           @click="logout">
              <v-icon>mdi-logout</v-icon>
              </v-btn>

          </v-list-item>

      </template>
    </v-navigation-drawer>

</template>

<script>
export default {
  name: 'c-menu',
  data () {
    return {
      selectedItem: 0,
      items: [
        { text: 'Главная', icon: 'mdi-home', path: '/' },
        { text: 'Товары', icon: 'mdi-calendar', path: '/calendar' },
        { text: 'Клиенты', icon: 'mdi-account-multiple', path: '/customers' },
        { text: 'Категории', icon: 'mdi-folder-multiple', path: '/category' },
        { text: 'Сотрудники', icon: 'mdi-clipboard-account', path: '/employee' },
        { text: 'Авторизация', icon: 'mdi-clipboard-account', path: '/auth' }
      ]
    }
  },
  methods: {
    logout () {
      this.$store.commit('setAuth', false)
      this.$cookies.remove('opt-token')
      this.$router.go()
    }
  }
}
</script>
