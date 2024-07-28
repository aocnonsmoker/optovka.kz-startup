<template>
    <div class="home">
        <div class="row">
            <div class="mt-5 col-md-4 category_list">
                <h3 class="text-center">Категории</h3>
                <b-list-group
                    class="align-left"
                    style="width: 100%; cursor: pointer"
                >
                    <b-list-group-item @click="clickCheck">
                        <b-avatar
                            src="https://arbuz.kz/image/s3/arbuz-kz-catalogs/225268-fermerskaya_lavka.png?w=%w&h=%h&_c=1710825195"
                            class="mr-3"
                        ></b-avatar>
                        <span class="mr-auto">Фермерская лавка</span>
                    </b-list-group-item>
                    <b-list-group-item>
                        <b-avatar
                            src="https://arbuz.kz/image/s3/arbuz-kz-catalogs/225165-hleb_vypechka.png?w=%w&h=%h&_c=1716015520"
                            class="mr-3"
                        ></b-avatar>
                        <span class="mr-auto">Хлеб, выпечка</span>
                    </b-list-group-item>
                    <b-list-group-item>
                        <b-avatar
                            src="https://arbuz.kz/image/s3/arbuz-kz-catalogs/14-napitki.png?w=%w&h=%h&_c=1712297613"
                            class="mr-3"
                        ></b-avatar>
                        <span class="mr-auto">Напитки</span>
                    </b-list-group-item>
                    <b-list-group-item>
                        <b-avatar
                            src="https://arbuz.kz/image/s3/arbuz-kz-catalogs/225161-moloko_syr_maslo_yaica.png?w=%w&h=%h&_c=1710825065"
                            class="mr-3"
                        ></b-avatar>
                        <span class="mr-auto">Молочная продукция</span>
                    </b-list-group-item>
                </b-list-group>
            </div>
            <div class="col-md-8 mt-5">
                <div class="promo">
                    <b-carousel
                        id="carousel-1"
                        v-model="slide"
                        :interval="4000"
                        controls
                        indicators
                        background="#ababab"
                        img-width="1024"
                        img-height="800"
                        style="text-shadow: 1px 1px 2px #333"
                        @sliding-start="onSlideStart"
                        @sliding-end="onSlideEnd"
                    >
                        <!-- Text slides with image -->
                        <b-carousel-slide>
                            <template v-slot:img>
                                <img
                                    src="https://magnum.kz:1337/uploads/2360h1016_a4e0e4bb74.jpg"
                                    alt="asd"
                                    width="730"
                                    height="570"
                                />
                            </template>
                        </b-carousel-slide>
                        <b-carousel-slide>
                            <template v-slot:img>
                                <img
                                    src="https://magnum.kz:1337/uploads/Banners_apps_2360h1016_RU_750e7adfff.jpg"
                                    alt="asd"
                                    width="730"
                                    height="570"
                                />
                            </template>
                        </b-carousel-slide>
                        <b-carousel-slide>
                            <template v-slot:img>
                                <img
                                    src="https://magnum.kz:1337/uploads/RU_2360h1016_1180x508_1d3d15d7b0.jpg"
                                    alt="asd"
                                    width="730"
                                    height="570"
                                />
                            </template>
                        </b-carousel-slide>
                    </b-carousel>
                </div>
                <div class="products mt-2">
                    <h3 class="text-center">Популярные продукты</h3>
                    <div class="row">
                        <div
                            class="col-md-4"
                            v-for="item in items"
                            :key="item.id"
                        >
                            <div class="item_info mt-3">
                                <img
                                    :src="item.image"
                                    width="186"
                                    height="186"
                                    alt="image"
                                    class="item_img"
                                />
                                <h3 class="item_name text-center">
                                    {{ item.name }}
                                </h3>
                                <h4 class="item_price text-center mt-3">
                                    {{ item.price }}₸
                                </h4>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// @ is an alias to /src

export default {
    name: 'Home',
    components: {
    },
    data() {
        return {
            slide: 0,
            sliding: null,
            items: [],
        }
    },
    created() {
        this.getProduct();
    },
    methods: {
        getProduct() {
            fetch('http://127.0.0.1:8000/market/product/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
                .then(res => this.items = res.sort((a, b) => a.name - b.name))
                .catch((error) => {
                    this.makeToast('danger', 'Ошибка запроса', error.toString());
                })
        },
        onSlideStart() {
            this.sliding = true
        },
        onSlideEnd() {
            this.sliding = false
        },
        clickCheck() {
            console.log('clicked')
        }
    }
}
</script>

<style>
.item_info {
    border: solid grey;
    border-radius: 20px;
}
.item_img {
    height: 180px;
    width: 180px;
    margin: 0 auto;
    display: block;
}
</style>
