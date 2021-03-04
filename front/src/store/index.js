import axios from 'axios'
import {
  Loading
} from 'quasar'

const BASE_URL = 'https://amk.of.by' // 'http://localhost:8000' // https://amk.of.by

let loading = false

let getterObj = function () {
  return this.state
}

let setterObj = function (arg, lang) {
  let url = ''
  if (this.endpoint && !arg) {
    url = `${BASE_URL}/api/${this.endpoint}?lang=${lang}`
  } else if (this.endpoint && arg) {
    url = `${BASE_URL}/api/${this.endpoint}/${arg}&lang=${lang}`
  }
  if (this.endpoint) {
    Loading.show()
    axios.get(url)
    .then((response) => {
      this.state = response.data
      Loading.hide()
    })
  }
}

let obj = {
  state: [],
  setObj: setterObj,
  getObj: getterObj
}

export default {
  sliders: {
    state: [],
    endpoint: 'sliders',
    __proto__: obj
  },
  index: {
    state: [],
    endpoint: 'index',
    __proto__: obj
  },
  products: {
    state: [],
    endpoint: 'products',
    __proto__: obj
  },
  categorylist: {
    state: [],
    endpoint: 'categorylist',
    __proto__: obj
  },
  product: {
    state: [],
    endpoint: 'products',
    __proto__: obj
  },
  news: {
    state: [],
    endpoint: 'news',
    __proto__: obj
  },
  delivery: {
    state: [],
    endpoint: 'page/1',
    __proto__: obj
  },
  contact: {
    state: [],
    endpoint: 'page/2',
    __proto__: obj
  },
  partners: {
    state: [],
    endpoint: 'page/3',
    __proto__: obj
  },
  about: {
    state: [],
    endpoint: 'page/4',
    __proto__: obj
  },
  new: {
    state: [],
    __proto__: obj
  }
}

export { BASE_URL }
