<template>
    <div class="main">
        <div class="row">
            <div class="widget col-md-5">Widget</div>
            <div class="widget col-md-5">Widget</div>
            <div class="widget col-md-5">Widget</div>
            <div class="widget col-md-5">Widget</div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
    }
  }
}
</script>

<style>
.main {
  margin-top: 30px;
}
.widget {
    height: 300px;
    width: 300px;
    background-color: grey;
    margin: 30px;
}
</style>
