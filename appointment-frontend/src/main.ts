import 'core-js/stable' // to polyfill ECMAScript features
import '@mdi/font/css/materialdesignicons.min.css' // icon library (https://materialdesignicons.com/)
import 'regenerator-runtime/runtime' // to use transpiled generator functions
import App from './App.vue'
import ConfigHelper from '@/utils/config-helper'
import TokenService from '@/services/token.services'
import Vue from 'vue'
import i18n from './plugins/i18n'
import router from './router'
import { store } from './store'
import vuetify from './plugins/vuetify'

Vue.config.productionTip = false
Vue.prototype.$tokenService = new TokenService()

/**
 * The server side configs are necessary for app to work , since they are reference in templates and all
 *  Two ways , either reload Vue after we get the settings or load vue after we get the configs..going for second
 */
ConfigHelper.saveConfigToSessionStorage().then((_data: any) => {
  renderVue()
})

function renderVue () {
  new Vue({
    router,
    vuetify,
    i18n,
    store,
    render: (h) => h(App)
  }).$mount('#app')
}