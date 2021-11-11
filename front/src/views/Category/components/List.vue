<template>
    <div>
        <ul>
            <li v-for="category in categories" :key="category.slug">
                {{ category.name }}
                <ul>
                    <li
                        v-for="brand in brands.filter(
                            (item) => item.category == category.id
                        )"
                        :key="brand.slug"
                    >
                        {{ brand.name }}
                        <ul>
                            <li
                                v-for="product in products.filter(
                                    (item) => item.brand == brand.id
                                )"
                                :key="product.slug"
                            >
                                <span
                                    style="cursor: pointer"
                                    @click="createOrder(product)"
                                    >{{ product.name }}</span
                                >
                                <div v-if="selectedProduct.id === product.id">
                                    <p>{{ selectedProduct.name }}</p>
                                    <span>Количество</span>
                                    <input
                                        v-model="qty"
                                        type="number"
                                        :min="selectedProduct.min_order"
                                    />
                                    <v-btn
                                        @click="saveOrder(selectedProduct)"
                                        color="primary"
                                        >Добавить</v-btn
                                    >
                                </div>
                            </li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ul>
        <div>
            <p v-for="ord in orders" :key="ord.id">
                Brand: {{ord.brand}} Product: {{ord.product}} Quantity: {{ord.qty}}
            </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'List',
    data() {
        return {
            categories: [],
            brands: [],
            products: [],
            selectedProduct: {},
            qty: null,
            order: {
                qty: null,
                product: null,
                brand: null,
            },
            orders: []
        }
    },
    methods: {
        getCategory() {
            fetch('http://127.0.0.1:8000/market/category/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
                .then(res => this.categories = res)
                .catch(error => console.log(error))
        },
        getBrand() {
            fetch('http://127.0.0.1:8000/market/brand/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
                .then(res => this.brands = res)
                .catch(error => console.log(error))
        },
        getProduct() {
            fetch('http://127.0.0.1:8000/market/product/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
                .then(res => this.products = res)
                .catch(error => console.log(error))
        },
        getOrders() {
            fetch('http://127.0.0.1:8000/market/order/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
            .then(res => this.orders = res.sort((a, b) => a.product - b.product))
            .catch(error => console.log(error))
        },
        createOrder(item) {
            console.log(item)
            this.selectedProduct = item
        },
        saveOrder(item) {
            this.order.product = item.id;
            this.order.brand = item.brand;
            this.order.qty = parseInt(this.qty);
            console.log(JSON.stringify(this.order))
            fetch('http://127.0.0.1:8000/market/order/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                },
                body: JSON.stringify(this.order)
            })
            .then(res => this.getOrders())
            .catch(error => console.log(error))
        }
    },
    created() {
        this.getCategory();
        this.getBrand();
        this.getProduct();
        this.getOrders();
    },
    mounted() {
        this.$watch('selectedProduct', () => {
            this.qty = this.selectedProduct.min_order
        })
    }
}
</script>