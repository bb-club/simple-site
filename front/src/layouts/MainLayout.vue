<template>
  <q-layout view="lHh lpR lff">
    <q-header reveal elevated class="text-black" height-hint="98" style="background-color: #009688e3 !important">
      <q-toolbar style="height: 75px;">
        <div class="col-12 row items-center" style="max-width: 1200px; margin: auto">
<!--          <q-btn size="md" flat round icon="menu" @click="left = !left" />-->
          <q-toolbar-title @click="$router.push({name: 'Index'})" v-ripple class="row col-shrink items-center cursor-pointer" style="position: relative; height: 75px"><q-avatar size="xl" icon="las la-drumstick-bite" /> amk.of.by </q-toolbar-title>
          <q-space />
          <q-select
            v-model="lang"
            :options="langOptions"
            :label="$t('language')"
            dense
            borderless
            emit-value
            map-options
            options-dense
            style="min-width: 150px"
          />
          <div class="gt-sm self-end row justify-center items-center no-wrap q-gutter-x-md">
            <q-icon size="sm" name="las la-phone-volume" />
            <div class="column text-subtitle2">
              <div> (029) 333-33-35 </div>
              <div> (044) 333-33-35 </div>
              <div> (017) 333-33-35 </div>
            </div>
          </div>
        </div>
      </q-toolbar>
      <div class="bg-deep-orange-7">
        <q-tabs align="center" class="width-block text-white">
          <q-route-tab icon="las la-drumstick-bite" :to="{name: 'Products'}" :label="$t('production')" />
          <q-route-tab icon="las la-truck" :to="{name: 'Delivery'}" :label="$t('delivery')" />
          <q-route-tab icon="las la-handshake" :to="{name: 'Partners'}" :label="$t('partners')" />
          <q-route-tab icon="las la-newspaper" :to="{name: 'News'}" :label="$t('news')" />
          <q-route-tab icon="las la-phone-volume" :to="{name: 'Contact'}" :label="$t('contacts')" />
        </q-tabs>
      </div>
    </q-header>

<!--    <q-drawer v-model="left" side="left" overlay behavior="mobile" bordered>-->
<!--      &lt;!&ndash; drawer content &ndash;&gt;-->
<!--    </q-drawer>-->

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
      <q-btn fab icon="keyboard_arrow_up" color="accent" />
    </q-page-scroller>

    <q-footer class="transparent">
      <div class="bg-white">
        <q-tabs align="center" class="text-black width-block">
          <q-route-tab :to="{name: 'Products'}" :label="$t('production')" />
          <q-route-tab :to="{name: 'Delivery'}" :label="$t('delivery')" />
          <q-route-tab :to="{name: 'Partners'}" :label="$t('partners')" />
          <q-route-tab :to="{name: 'News'}" :label="$t('news')" />
          <q-route-tab :to="{name: 'Contact'}" :label="$t('contacts')" />
        </q-tabs>
      </div>
    </q-footer>

  </q-layout>
</template>

<script>
export default {
  data () {
    return {
      left: false,
      lang: this.$i18n.locale,
      langOptions: [
        { value: 'ru', label: 'Русский' },
        { value: 'en', label: 'English' },
        { value: 'ch', label: '中文' }
      ]
    }
  },
  meta: {
    title: 'AMK.OF.BY'
  },
  watch: {
    lang(lang) {
      this.$i18n.locale = lang
      this.$q.localStorage.set('lang', lang)
    }
  }
}
</script>
