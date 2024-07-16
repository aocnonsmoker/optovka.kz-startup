<template>
    <div class="mt-3 mr-5">
        <h1>Заказы</h1>
    </div>
</template>

<script>
export default {
    name: 'Orders',
    data() {
        return {
            orders: [],
            brand_id: 1
        }
    },
    created() {
        this.getOrders();
    },
    methods: {
        getOrders() {
            // axios({
            //     method: 'get',
            //     url: `http://127.0.0.1:8000/market/order`,
            //     headers: {
            //         'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
            //     },
            //     data: {
            //         'brand': this.brand_id
            //     }
            // })
            //     .then((request) => {
            //         console.log(request.data)
            //     })
            fetch('http://127.0.0.1:8000/market/order/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => console.log(res))
                .catch((error) => {
                    this.makeToast('danger', 'Ошибка запроса', error.toString());
                })
        }
    },

}
</script>
