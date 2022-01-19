<template>
<div class="w-full bg-gray-200 h-screen">

            <div class="bg-white m-5">
                <div class="p-5">
                    <h1>Добро пожаловать в <span class="font-bold uppercase">YonaCRM</span> </h1>
                    текущая версия приложения: 1.0.0.1

                </div>
            </div>

                  <div class="bg-white m-5">
                <div class="p-5">
                </div>
            </div>
        </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      chartOptions: {
        title: {
          text: 'Общее количество заявок'
        },
        xAxis: {
          categories: []
        },
        credits: {
          enabled: false
        },
        series: [{
          data: [] // sample data
        }]
      },
      events: []
    }
  }
}
</script>
