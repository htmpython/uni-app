import App from './App'

// #ifndef VUE3
import Vue from 'vue'
import './uni.promisify.adaptor'
import uView from '@/uni_modules/uview-ui'
Vue.use(uView)

// 注册vue原型链
import request from './components/request.js'
Vue.prototype.$request = request
// 注册公共方法
import public_ from './components/public.js'
Vue.prototype.$public = public_


Vue.config.productionTip = false
App.mpType = 'app'
const app = new Vue({
  ...App
})
app.$mount()
// #endif

// #ifdef VUE3
import { createSSRApp } from 'vue'
export function createApp() {
  const app = createSSRApp(App)
  return {
    app
  }
}
// #endif