<template>
  <q-page padding class="column">
    <div style="height: 700px">
      <q-pdfviewer
        class="col-12"
        :value="true"
        :src="getUrl"
        type="pdfjs"
      />
    </div>
  </q-page>
</template>

<script>
import { BASE_URL } from 'src/store'

export default {
  name: 'Requisites',
  computed: {
    getUrl() {
      return BASE_URL+'/img/recv.pdf'
    }
  }
}
</script>
