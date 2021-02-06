<template>
  <q-page padding>
    <div class="width-block" v-html="$store.partners.getObj().text"></div>
  </q-page>
</template>

<script>
export default {
  name: 'Partners',
  watch: {
    '$i18n.locale': function f() {
      this.$store.partners.setObj(null, this.$i18n.locale)
    }
  },
  created() {
    this.$store.partners.setObj(null, this.$i18n.locale)
  }
}
</script>
