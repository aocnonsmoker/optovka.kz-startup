<template>
    <div>
        <b-nav vertical class="menu w-100">
          <b-nav-item to="/" class="menu_item">Главное</b-nav-item>
          <b-nav-item to="/products" class="menu_item">Товары</b-nav-item>
          <b-nav-item to="/orders" class="menu_item">Заказы</b-nav-item>
          <b-nav-item to="/clients" class="menu_item">Клиенты</b-nav-item>
          <b-nav-item to="/staff" class="menu_item">Сотрудники</b-nav-item>
          <b-nav-item to="/stock" class="menu_item">Склад</b-nav-item>
          <b-nav-item to="/profile" class="menu_item">Профиль</b-nav-item>
        </b-nav>
    </div>
</template>

<script>
export default {
    name: 'CMenu'
}
</script>

<style>
    
    .menu .menu_item {
        margin: 20px;
    }
</style>