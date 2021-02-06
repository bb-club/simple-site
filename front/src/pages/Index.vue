<template>
  <q-page class="relative-position" style="top:-147px; margin-bottom: -147px">
    <q-card tag="div" class="bg-secondary">
      <q-carousel
        height="650px"
        animated
        transition-prev="jump-up"
        transition-next="jump-down"
        swipeable
        v-model="slide"
        infinite
        :autoplay="autoplay"
        @mouseenter="autoplay = false"
        @mouseleave="autoplay = true"
      >
        <q-carousel-slide v-for="(slide , index) in $store.sliders.getObj()" :name="index" :key="slide.id" :img-src="slide.image_src">
          <div class="absolute-bottom custom-caption">
            <div class="text-h2 text-secondary">{{ slide.title }}</div>
            <div class="text-subtitle1">{{ slide.description }}</div>
          </div>
        </q-carousel-slide>
      </q-carousel>
    </q-card>
    <div>
      <div class="text-h4 text-center text-grey" style="margin: auto"> Основные категории </div>
      <div class="row width-block">
        <div v-for="(product, i) in $store.index.getObj()" class="col-sm-4 col-12" :key="i">
          <q-card v-ripple class="my-card q-ma-sm cursor-pointer bg-secondary" @click="$router.push('#')">
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
  watch: {
    '$i18n.locale': function () {
      this.$store.sliders.setObj(null, this.$i18n.locale)
    }
  },
  created() {
    this.$store.sliders.setObj(null, this.$i18n.locale)
    this.$store.index.setObj(null, this.$i18n.locale)
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
