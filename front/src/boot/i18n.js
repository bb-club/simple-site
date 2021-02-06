import Vue from 'vue'
import VueI18n from 'vue-i18n'

import messages from 'src/i18n'
import { LocalStorage } from 'quasar'

let lang = LocalStorage.getItem('lang') || 'ru'

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: lang,
  fallbackLocale: lang,
  messages
})

export default ({ app }) => {
  // Set i18n instance on app
  app.i18n = i18n
}

// if you need to import it from
// other files, then:
export { i18n }
