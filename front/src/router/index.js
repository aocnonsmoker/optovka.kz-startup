import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/auth',
    name: 'Auth',
    component: () => import('../views/Auth/Auth.vue')
  },
  {
    path: '/category',
    name: 'Category',
    component: () => import('../views/Category/Category.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile/Profile.vue')
  },
  {
    path: '/test',
    name: 'Test',
    component: () => import('../views/Test.vue')
  },
]

const router = new VueRouter({
  routes
})

export default router
