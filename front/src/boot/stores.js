import Vue from 'vue'
import model from '../store/index'

Vue.prototype.$store = Vue.observable(model)
window.store = model
