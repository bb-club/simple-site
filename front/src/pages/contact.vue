<template>
  <q-page padding>
    <div class="width-block column">
      <div v-html="$store.contact.getObj().text"></div>
      <yandex-map zoom="12" :coords="coords" style="height: 400px">
        <ymap-marker
        marker-id="123"
        :coords="coords"
        :balloon-template="balloonTemplate"
        />
      </yandex-map>
    </div>
  </q-page>
</template>

<script>
import { yandexMap, ymapMarker } from 'vue-yandex-maps'

export default {
  name: 'Contact',
  components: { yandexMap, ymapMarker },
  data() {
    return {
      coords: [53.99221754, 27.67741442],
      balloonTemplate: 'Мы здесь'
    }
  },
  watch: {
    '$i18n.locale': function f() {
      this.$store.contact.setObj(null, this.$i18n.locale)
    }
  },
  created() {
    this.$store.contact.setObj(null, this.$i18n.locale)
  }
}
</script>
