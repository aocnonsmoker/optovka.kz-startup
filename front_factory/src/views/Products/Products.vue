<template>
    <div class="mt-3 mr-5">
        <h1>Товары</h1>
        <b-form-select v-model="selectedCategory">
            <option
                v-for="category in categoriesList"
                :key="category.id"
                :value="category"
            >
                {{ category.name }}
            </option>
        </b-form-select>
        <b-btn variant="success" v-b-modal.newItem class="addItem_btn"
            >Добавить товар</b-btn
        >
        <b-modal id="newItem" centered hide-footer>
            <b-form-group
                label="Выберите картинку"
            >
                <b-form-file
                    v-model="newImage"
                    :state="Boolean(newImage)"
                    required
                ></b-form-file>
            </b-form-group>

            <b-form-group
                label="Наименование товара"
            >
                <b-form-input
                    v-model="newName"
                    type="text"
                    required
                ></b-form-input>
            </b-form-group>

            <b-form-group
                label="Описание товара"
            >
                <b-form-textarea
                    v-model="newDescription"
                ></b-form-textarea>
            </b-form-group>

            <b-form-group
                label="Цена товара"
            >
                <b-form-input
                    v-model="newPrice"
                    type="number"
                    prefix="₸"
                    required
                ></b-form-input>
            </b-form-group>

            <b-form-group
                label="Минимальное количество за заказ"
            >
                <b-form-input
                    v-model="newMinOrder"
                    type="number"
                    required
                ></b-form-input>
            </b-form-group>

            <b-form-group
                label="Выберите категорию"
            >
                <b-form-select
                    v-model="newItemCategory"
                    :options="categoriesList"
                    required
                    value-field="id"
                    text-field="name"
                ></b-form-select>
            </b-form-group>
            <b-button class="mt-3" variant="outline-success" block @click="saveItem">Сохранить</b-button>
            <b-button class="mt-2" variant="outline-secondary" block @click="$bvModal.hide('newItem')">Отменить</b-button>
        </b-modal>

        <div class="itemList row">
            <div class="item col-md-3" v-for="item in itemList" :key="'item_' + item.id">
                <div class="item_info">
                    <img :src="item.image" alt="image" class="item_img">
                    <h3 class="item_name text-center">{{ item.name }} - {{ item.description }}</h3>
                    <h4 class="item_price text-center mt-3">{{ item.price }}₸</h4>
                    <h4 class="item_price text-center mt-3">Заказ от: {{ item.min_order }} шт.</h4>
                    <h5 class="item_quantity text-center">В наличий: 249 шт.</h5>
                </div>
                <div class="item_edit">
                    <b-button v-b-modal="'editItem_' + item.id" variant="outline-warning" class="edit m-2"><b-icon icon="pencil-fill"></b-icon></b-button>
                    <b-button v-b-modal="'deleteItem_' + item.id" variant="outline-danger" class="delete m-2"><b-icon icon="trash-fill"></b-icon></b-button>
                </div>
                <b-modal :id="`editItem_${item.id}`" centered hide-footer>
                    <img class="item_img" :src="item.image">
                    <b-form-group
                        label="Выберите картинку"
                    >
                        <b-form-file
                            v-model="item.image"
                            :state="Boolean(item.image)"
                            required
                        ></b-form-file>
                    </b-form-group>

                    <b-form-group
                        label="Наименование товара"
                    >
                        <b-form-input
                            v-model="item.name"
                            type="text"
                            required
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group
                        label="Описание товара"
                    >
                        <b-form-textarea
                            v-model="item.description"
                        ></b-form-textarea>
                    </b-form-group>

                    <b-form-group
                        label="Цена товара"
                    >
                        <b-input-group>
                            <b-form-input
                                v-model="item.price"
                                type="number"
                                required
                            ></b-form-input>
                            <b-input-group-append>
                                <b-input-group-text class="bg-transparent font-weight-bold">
                                    ₸
                                </b-input-group-text>
                            </b-input-group-append>
                        </b-input-group>
                    </b-form-group>

                    <b-form-group
                        label="Минимальное количество за заказ"
                    >
                        <b-form-input
                            v-model="item.min_order"
                            type="number"
                            required
                        ></b-form-input>
                    </b-form-group>

                    <b-form-group
                        label="Выберите категорию"
                    >
                        <b-form-select
                            v-model="item.category"
                            :options="categoriesList"
                            required
                            value-field="id"
                            text-field="name"
                        ></b-form-select>
                    </b-form-group>
                    <b-button class="mt-3" variant="outline-success" block @click="editItem(item)">Сохранить</b-button>
                    <b-button class="mt-2" variant="outline-secondary" block @click="$bvModal.hide('editItem_' + item.id)">Отменить</b-button>
                </b-modal>
                <b-modal :id="`deleteItem_${item.id}`">
                    <div class="item_delete">
                        <div>Вы действительно хотите удалить?</div>
                        <b-button variant="outline-secondary" block @click="$bvModal.hide('deleteItem_' + item.id)" class="edit m-2">Нет</b-button>
                        <b-button variant="outline-danger" block @click="deleteItem(item.id)" class="delete m-2">Да</b-button>
                    </div>
                </b-modal>
            </div>
        </div>
        <loading
            :active="loading"
            is-full-screen
            spinner="bar-fade-scale"
            color="#6495ED"
        />
    </div>
</template>

<script>
import VueElementLoading from "vue-element-loading";
import axios from 'axios';
export default {
    name: 'Items',
    components: { 'loading': VueElementLoading },
    data() {
        return {
            items: [],
            itemList: [],
            dialog: false,
            saveImage: null,
            newDialog: false,
            newName: null,
            newDescription: null,
            newPrice: null,
            newImage: null,
            newMinOrder: 1,
            newItemCategory: null,
            categoriesList: [],
            selectedCategory: {
                id: null,
                name: 'Все',
                slug: ''
            },
            loading: false
        }
    },
    created() {
        this.getProduct();
        this.getCategory();
    },
    mounted() {
        this.$watch('selectedCategory', () => {
            if (this.selectedCategory.id) {
                this.itemList = this.items.filter(x => x.category === this.selectedCategory.id)
            } else {
                this.itemList = this.items
            }
        })
    },
    methods: {
        getCategory() {
            fetch('http://127.0.0.1:8000/market/category/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
            .then(res => this.categoriesList = res.sort((a, b) => a.name - b.name))
            .then(() => this.categoriesList.unshift({
                    id: null,
                    name: 'Все',
                    slug: ''
            }))
            .catch(error => console.log(error))
        },
        getProduct() {
            fetch('http://127.0.0.1:8000/market/product/', {
                method: 'GET',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            }).then(res => res.json())
                .then(res => this.items = res.sort((a, b) => a.name - b.name))
                .then(() => this.itemList = [...this.items])
                .catch((error) => {
                    this.makeToast('danger', 'Ошибка запроса', error.toString());
                })
        },
        async editItem(item) {
            this.loading = true;
            this.$bvModal.hide('editItem_' + item.id)
            const fd = new FormData();
            fd.append('name', item.name)
            fd.append('description', item.description)
            fd.append('price', Number(item.price))
            fd.append('id', item.id)
            fd.append('image', item.image)
            fd.append('min_order', item.min_order)
            fd.append('category', item.category)
            await axios({
                method: 'patch',
                url: `http://127.0.0.1:8000/market/product/${item.id}/`,
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                },
                data: fd
            })
                .then(() => {
                    this.getProduct();
                })
                .catch((error) => {
                    this.makeToast('danger', 'Ошибка запроса', error.toString());
                })
            this.loading = false;
        },
        saveItem() {
            this.loading = true;
            const fd = new FormData();
            if (this.newImage) {
                fd.append('image', this.newImage, this.newImage.name)
            }
            fd.append('name', this.newName)
            fd.append('description', this.newDescription)
            fd.append('price', this.newPrice)
            fd.append('min_order', this.newMinOrder),
            fd.append('category', this.newItemCategory)
            axios({
                method: 'post',
                url: 'http://127.0.0.1:8000/market/product/',
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                },
                data: fd
            })
                .then(() => {
                    this.$bvModal.hide('newItem')
                    this.getProduct();
                    this.loading = false;
                    this.newImage = null;
                    this.newName = null;
                    this.newDescription = null;
                    this.newPrice = null;
                    this.newMinOrder = 1;
                    this.newItemCategory = null;
                    this.makeToast('success', 'Сохранено', 'Товар успешно сохранен');
                })
                .catch((error) => {
                    this.makeToast('danger', 'Ошибка запроса', error.toString());
                    this.loading = false;
                })
        },
        deleteItem(id) {
            axios({
                method: 'delete',
                url: `http://127.0.0.1:8000/market/product/${id}/`,
                headers: {
                    'Authorization': 'Token e32616f634eb2f11d9bc6586df19daf1648f208d'
                }
            })
                .then(() => {
                    this.getProduct();
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
        },
    }
}
</script>

<style>
.itemsList {
    background-color: #f5f5f5;
    width: 100%;
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}
.item {
    border: solid white;
    border-radius: 20px;
    margin: 10px 20px;
    width: 500px;
    text-align: center;
}
.item_img {
    height: 180px;
    width: 180px;
    margin: 0 auto;
    display: block;
}
.addItem_btn {
    margin: 10px 0 20px 0;
}

.edit_btn {
    margin: 5px;
}
</style>