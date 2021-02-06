<template>
  <q-page padding>
    <div class="width-block" v-html="$store.delivery.getObj().text"></div>
  </q-page>
</template>

<script>
export default {
  name: 'Delivery',
  watch: {
    '$i18n.locale': function f() {
      this.$store.delivery.setObj(null, this.$i18n.locale)
    }
  },
  created() {
    this.$store.delivery.setObj(null, this.$i18n.locale)
  }
}
</script>
