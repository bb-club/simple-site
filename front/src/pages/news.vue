<template>
  <q-page padding class="width-block">
    <q-card v-for="statya in $store.news.getObj()" :key="statya.id">
      <q-card-section v-html="statya.text" :style="show ? '': 'max-height: 300px; overflow: hidden;'">
      </q-card-section>
      <q-card-actions>
        <q-btn :label="show ? 'Скрыть подробности': 'Подробнее'" @click="show = !show" />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<script>
export default {
  name: 'News',
  data() {
    return {
      show: false
    }
  },
  watch: {
    '$i18n.locale': function f() {
      this.$store.news.setObj(null, this.$i18n.locale)
    }
  },
  created() {
    this.$store.news.setObj(null, this.$i18n.locale)
  }
}
</script>
