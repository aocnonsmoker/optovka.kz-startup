<template>
    <div id="app">
        <div class="row">
            <div class="col-md-2">
                <c-menu />
            </div>
            <div class="col-md-10">
                <div>
                    <router-view />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CMenu from './components/c-menu'
export default {
    name: 'App',
    components: { CMenu },
    data: () => ({
        //
    })
}
</script>
