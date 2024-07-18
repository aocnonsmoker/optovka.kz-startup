<template>
    <div class="mt-3 mr-5">
        <h1>Заказы</h1>
        <b-form-select class="mt-2 mb-2" v-model="selectedStatus">
            <option
                v-for="status in statusList"
                :key="status.id"
                :value="status"
            >
                {{ status.name }}
            </option>
        </b-form-select>
        <b-table head-variant="dark" :fields="fields" :items="orderList">
            <template #cell(image)="data">
                <div><img height="100" width="100" :src="'http://127.0.0.1:8000/products/' + data.item.image"></div>
            </template>
            <template #cell(created_date)="data">
                <div>{{ getDate(data.item.created_date) }}</div>
            </template>
            <template #cell(updated_date)="data">
                <div>{{ getDate(data.item.updated_date) }}</div>
            </template>
            <template #cell(status)="data">
                <div>{{ statusList.find(a => a.code === data.item.status).name }}</div>
            </template>
            <template #cell(action)="data">
                <b-dropdown dropleft class="more-dropdown">
                    <template v-slot:button-content>
                        <i class="icon icon-more"></i>
                    </template>
                    <template>
                        <b-dropdown-item v-for="st in statusList.filter(x => x.code > 1)" :key="st.code + '_' + data.item.id" :disabled="st.code === data.item.status" @click="chgStatus(data.item.id, st.code)">
                            {{ st.name }}
                        </b-dropdown-item>
                    </template>
                </b-dropdown>
            </template>
        </b-table>
    </div>
</template>

<script>
import moment from 'moment';
import axios from 'axios';
export default {
    name: 'Orders',
    data() {
        return {
            orders: [],
            orderList: [],
            brand_id: 1,
            fields: [
                {
                    'label': 'Картинка',
                    'key': 'image'
                },
                {
                    'label': 'Товар',
                    'key': 'product'
                },
                {
                    'label': 'Количество',
                    'key': 'count'
                },
                {
                    'label': 'Магазин',
                    'key': 'market'
                },
                                {
                    'label': 'Адрес',
                    'key': 'market_address'
                },
                {
                    'label': 'Контакты',
                    'key': 'market_contact'
                },
                {
                    'label': 'Дата создания заказа',
                    'key': 'created_date'
                },
                {
                    'label': 'Дата редактирования заказа',
                    'key': 'updated_date'
                },
                {
                    'label': 'Статус заказа',
                    'key': 'status'
                },
                {
                    'label': ' ',
                    'key': 'action'
                }
            ],
            statusList: [
                {
                    'code': 0,
                    'name': 'Все'
                },
                {
                    'code': 1,
                    'name': 'Создан'
                },
                {
                    'code': 2,
                    'name': 'Принят'
                },
                {
                    'code': 3,
                    'name': 'Отправлен'
                },
                {
                    'code': 4,
                    'name': 'Отменен'
                }
            ],
            selectedStatus: {
                'code': 0,
                'name': 'Все'
            }
        }
    },
    created() {
        this.getOrders();
    },
    mounted() {
        this.$watch('selectedStatus', () => {
            if (this.selectedStatus.code) {
                this.orderList = this.orders.filter(x => x.status === this.selectedStatus.code)
            } else {
                this.orderList = this.orders
            }
        })
    },
    methods: {
        getOrders() {
            fetch('http://127.0.0.1:8000/market/order/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
            .then(res => this.orders = res)
            .then(() => {
                if (this.selectedStatus.code) {
                    this.orderList = this.orders.filter(x => x.status === this.selectedStatus.code)
                } else {
                    this.orderList = this.orders
                }
            })
            .catch((error) => {
                this.makeToast('danger', 'Ошибка запроса', error.toString());
            })
        },
        getDate(date) {
            return moment(String(date)).format('DD/MM/YYYY hh:mm')
        },
        chgStatus(id, code) {
            const fd = new FormData();
            fd.append('id', id)
            fd.append('status', code)
            axios({
                method: 'patch',
                url: `http://127.0.0.1:8000/market/order/${id}/`,
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                },
                data: fd
            })
                .then(() => {
                    this.getOrders();
                })
                .catch((error) => {
                    this.makeToast('danger', 'Ошибка запроса', error.toString());
                })
        },
        makeToast(variant, title, tostbody) {
            this.$bvToast.toast(tostbody, {
                title: title,
                variant: variant,
                toaster: 'b-toaster-top-center',
                autoHideDelay: 5000,
                appendToast: true
            });
        }
    },

}
</script>
