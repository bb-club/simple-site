<template>
  <q-page class="relative-position" style="top:-147px; margin-bottom: -147px">
    <q-card flat tag="div" class="bg-secondary">
      <q-carousel
        animated
        transition-prev="jump-up"
        transition-next="jump-down"
        swipeable
        v-model="slide"
        infinite
        thumbnails
        :autoplay="autoplay"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
        :style="'margin-top:' + ($q.screen.lt.md ? '55px': '115px')"
      >
        <q-carousel-slide v-for="(slide , index) in $store.sliders.getObj()" :name="index" :key="slide.id" :img-src="slide.image_src" />
      </q-carousel>
    </q-card>
    <div>
      <div class="row width-block">
        <div class="q-mt-md text-body1 text-grey-8" v-html="$store.about.getObj().text"></div>
        <div class="text-h5 text-center text-grey full-width" style="margin: auto"> {{ $t('categories') }} </div>
        <div v-for="(product, i) in $store.index.getObj()" class="col-sm-4 col-12" :key="i">
          <q-card v-ripple class="my-card q-ma-sm cursor-pointer bg-secondary" @click="goCategory(product.category)">
            <q-img :src="product.image_src" height="233px" />
            <q-card-section>
              <div class="row no-wrap items-center justify-center">
                <div class="col text-h6 text-center text-white ellipsis">
                  {{  product.title }}
                </div>
              </div>
            </q-card-section>
            <q-card-section v-if="product.description" class="q-pt-none">
              <div class="text-caption text-grey">
                {{  product.description }}
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>

  </q-page>
</template>

<script>
export default {
  name: 'PageIndex',
  data () {
    return {
      slide: 1,
      autoplay: true
    }
  },
  methods: {
    goCategory (id) {
      this.$router.push({name: 'Products', query: { filter: id }})
    }
  },
  watch: {
    '$i18n.locale': function () {
      this.$store.sliders.setObj(null, this.$i18n.locale)
      this.$store.index.setObj(null, this.$i18n.locale)
      this.$store.about.setObj(null, this.$i18n.locale)
    }
  },
  created() {
    this.$store.sliders.setObj(null, this.$i18n.locale)
    this.$store.index.setObj(null, this.$i18n.locale)
    this.$store.about.setObj(null, this.$i18n.locale)
  }
}
</script>

<style lang="sass" scoped>
.custom-caption
  text-align: center
  padding: 12px
  color: white
  background-color: rgba(0, 0, 0, .1)
</style>
