<template>
  <q-page padding>
    <q-img :src="$store.BASE_URL"
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
