<template>
    <div>
        <h1>Category page</h1>
        <list />
    </div>
</template>

<script>
import List from './components/List'
export default {
  name: 'Category',
  components: {
    list: List
  }
}
</script>
