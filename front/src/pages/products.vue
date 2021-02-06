<template>
  <q-page padding>
    <div class="row width-block">
      <div class="row col-12 justify-between">
        <q-select
            filled
            v-model="filter"
            :options="optionsGet"
            dense
            :label="labelGet"
            multiple
            emit-value
            map-options
            style="width: 220px;"
        >
          <template v-slot:option="scope">
            <q-item v-bind="scope.itemProps" v-on="scope.itemEvents">
              <q-item-section>
                <q-item-label v-html="scope.opt.label" ></q-item-label>
              </q-item-section>
              <q-item-section side>
                <q-toggle v-model="filter" :val="scope.opt.value" />
              </q-item-section>
            </q-item>
          </template>
        </q-select>
        <q-pagination
          v-model="page"
          color="purple"
          :max="Math.ceil(productsGet.count/10)"
          :max-pages="3"
          :boundary-numbers="true"
        ></q-pagination>
      </div>
      <div v-for="(product, i) in productsGet.results" class="col-12" :key="i">
         <q-card class="my-card q-my-sm">
          <div style="overflow-x: auto">
            <q-img contain :src="product.image_src" height="220px" :width="'1100px'" />
          </div>
          <q-card-section>
            <div class="row no-wrap items-center">
              <div class="col text-h6 ellipsis">
                {{  product.name }}
              </div>
            </div>
          </q-card-section>
          <q-card-section class="q-pt-none">
            <div class="text-subtitle1" v-text="$t(product.category.name)">
            </div>
            <div class="text-caption text-grey">
              {{  product.description }}
            </div>
          </q-card-section>
<!--            <q-separator />-->
<!--            <q-card-actions align="right">-->
<!--              <q-btn icon="las la-hand-pointer" flat color="primary">-->
<!--                Подробнее-->
<!--              </q-btn>-->
<!--            </q-card-actions>-->
        </q-card>
      </div>
      <div class="column col-12 items-end">
        <q-pagination
          v-model="page"
          color="purple"
          :max="Math.ceil(productsGet.count/10)"
          :max-pages="3"
          :boundary-numbers="true"
        ></q-pagination>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Products',
   data () {
    return {
      slide: 1,
      page: 1,
      autoplay: true,
      filter: [],
      label: this.$t('filter')
    }
  },
  computed: {
    labelGet() {
      return this.$t('filter')
    },
    optionsGet () {
      let category = this.$store.categorylist.getObj()
      category = category.filter(x => x.status)
      category = category.map((item) => { return { label: this.$t(item.name), value: item.id } })
      return category
    },
    productsGet() {
      return this.$store.products.getObj()
    },
  },
  methods: {
    productSet() {
      let params = ''
      if (this.filter.length) {
        params = '?category=' + this.filter.join('&category=') + '&'
      } else {
        params = '?'
      }
      this.$store.products.setObj(params + `page=${this.page}`, this.$i18n.locale)
    }
  },
  watch: {
    filter: function () {
      this.page = 1
      this.productSet()
    },
    page: function () {
      this.productSet()
    },
    '$i18n.locale': function f() {
      this.productSet()
    }
  },
  created() {
    this.$store.categorylist.setObj(null, this.$i18n.locale)
    this.$store.products.setObj(null, this.$i18n.locale)
  }
}
</script>
