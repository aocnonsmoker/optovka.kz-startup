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
    path: '/orders',
    name: 'Orders',
    component: () => import('../views/Orders/Orders.vue')
  },
  {
    path: '/products',
    name: 'Products',
    component: () => import('../views/Products/Products.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile/Profile.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
