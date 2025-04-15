import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import router from './router'

const app = createApp(App)

// 配置 axios 默认值
axios.defaults.baseURL = ''
axios.defaults.timeout = 30000
axios.defaults.headers.common['Content-Type'] = 'application/json'
axios.defaults.withCredentials = true

app.use(ElementPlus)
app.use(router)
app.config.globalProperties.$axios = axios
app.mount('#app')