<template>
    <header>
        <nav>
            <div class="container">
                <ul class="menu">
                    <li class="menu_item"><a href="#" class="menu_link">Главная</a></li>
                    <li class="menu_item"><a href="#" class="menu_link">Категории</a></li>
                    <li class="menu_item"><a href="#" class="menu_link">Избранные</a></li>
                    <li class="menu_item"><a href="#" class="menu_link">Корзина</a></li>
                    <li class="menu_item"><a href="#" class="menu_link">Профиль</a></li>
                </ul>
            </div>
        </nav>
    </header>
</template>

<style>
header {
    position: relative;
}

nav {
    height: 50px;
    background-color: #212121;
}

.menu {
    display: flex;
    justify-content: space-between;
    padding: 13px 70px;
    margin: 0;
    list-style-type: none;
}

.menu .menu_link {
    color: #ffffff;
    font-size: 15px;
    font-weight: 300;
}

</style>
