<template>
    <v-app>
        <v-card>
            <v-navigation-drawer permanent>
                <v-list-item>
                    <v-list-item-content>
                        <v-list-item-title class="text-h6">
                            Company name
                        </v-list-item-title>
                        <v-list-item-subtitle>
                            Firstname Lastname
                        </v-list-item-subtitle>
                    </v-list-item-content>
                </v-list-item>

                <v-divider></v-divider>

                <v-list dense nav>
                    <v-list-item
                        v-for="item in items"
                        :key="item.title"
                        link
                        @click="changePath(item.href)"
                    >
                        <v-list-item-icon>
                            <v-icon>{{ item.icon }}</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content>
                            <v-list-item-title>{{
                                item.title
                            }}</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-navigation-drawer>
        </v-card>
        <v-main>
            <router-view />
        </v-main>
    </v-app>
</template>

<script>

export default {
    name: 'App',
    data() {
        return {
            drawer: false,
            items: [
                { title: 'Профиль', icon: 'mdi-account', href: '/profile' },
                { title: 'Авторизация', icon: 'mdi-login', href: '/auth' },
                { title: 'Категории', icon: 'mdi-image', href: '/category' },
                { title: 'About', icon: 'mdi-help-box', href: '/' }
            ],
            right: null
        }
    },
    methods: {
        changePath(path) {
            this.$router.push(path)
        }
    }
}
</script>
