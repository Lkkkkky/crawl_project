<template>
  <div class="app">
    <Sidebar @menu-change="handleMenuChange" />
    <div class="content">
      <GoodsList v-show="currentMenu === 'search'" :goodsList="goodsList" :total="total" :loading="loading"
        @search="handleSearch" @update:goodsList="updateGoodsList" />
      <BrowsingHistory v-show="currentMenu === 'history'" />
      <Favorites v-show="currentMenu === 'favorites'" />
      <div v-show="currentMenu === 'recommendations'" class="recommendations">
        <div class="button-group">
          <el-button type="primary" @click="generateRecommendations" :loading="generatingRecommendations">
            生成推荐商品
          </el-button>
          <el-button type="danger" @click="clearRecommendations" :loading="clearingRecommendations">
            清空推荐
          </el-button>
        </div>
        <div class="recommendations-list">
          <el-card v-for="item in recommendationList" :key="item.good_url" class="recommendation-item">
            <h3>{{ item.good_name }}</h3>

            <p>来源: {{ item.good_source }}</p>
            <el-button type="text" @click="window.open(item.good_url, '_blank')">查看详情</el-button>
            <el-button type="danger" @click="deleteRecommendation(item.good_url)"
              :loading="deletingItem === item.good_url">
              <el-icon>
                <Delete />
              </el-icon>
              删除
            </el-button>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'
import Sidebar from './Sidebar.vue'
import GoodsList from './GoodsList.vue'
import BrowsingHistory from './BrowsingHistory.vue'
import Favorites from './Favorites.vue'
import { Delete } from '@element-plus/icons-vue'

const currentMenu = ref('search')
const goodsList = ref([])
const total = ref(0)
const loading = ref(false)
const recommendationList = ref([])
const generatingRecommendations = ref(false)
const clearingRecommendations = ref(false)

const handleMenuChange = (menu) => {
  currentMenu.value = menu
  if (menu === 'recommendations') {
    fetchRecommendations()
  }
}

const handleSearch = async (params) => {
  loading.value = true
  try {
    const response = await axios.get('/api/goods/search', { params })
    goodsList.value = response.data.list
    total.value = response.data.total
  } catch (error) {
    console.error('搜索失败:', error.response?.data || error)
    ElMessage.error(error.response?.data?.message || '搜索失败，请稍后重试')
  } finally {
    loading.value = false
  }
}

const updateGoodsList = (newList) => {
  goodsList.value = newList
}

const generateRecommendations = async () => {
  generatingRecommendations.value = true
  try {
    const username = localStorage.getItem('username')
    await axios.post(`/api/recommendations/generate?username=${username}`)
    await fetchRecommendations()
    ElMessage.success('推荐商品生成成功')
  } catch (error) {
    console.error('生成推荐商品失败:', error.response?.data || error)
    ElMessage.error(error.response?.data?.message || '生成推荐商品失败，请稍后重试')
  } finally {
    generatingRecommendations.value = false
  }
}

const fetchRecommendations = async () => {
  try {
    const username = localStorage.getItem('username')
    const response = await axios.get(`/api/recommendations/list?username=${username}`)
    recommendationList.value = response.data
  } catch (error) {
    console.error('获取推荐商品失败:', error.response?.data || error)
    ElMessage.error(error.response?.data?.message || '获取推荐商品失败，请稍后重试')
  }
}

const clearRecommendations = async () => {
  clearingRecommendations.value = true
  try {
    const username = localStorage.getItem('username')
    await axios.delete(`/api/recommendations/clear?username=${username}`)
    recommendationList.value = []
    ElMessage.success('推荐商品已清空')
  } catch (error) {
    console.error('清空推荐失败:', error.response?.data || error)
    ElMessage.error(error.response?.data?.message || '清空推荐失败，请稍后重试')
  } finally {
    clearingRecommendations.value = false
  }
}

const deletingItem = ref(null)

const deleteRecommendation = async (goodUrl) => {
  deletingItem.value = goodUrl
  try {
    const username = localStorage.getItem('username')
    await axios.delete(`/api/recommendations/remove?username=${username}&goodUrl=${goodUrl}`)
    await fetchRecommendations()
    ElMessage.success('删除推荐商品成功')
  } catch (error) {
    console.error('删除失败:', error.response?.data || error)
    ElMessage.error(error.response?.data?.message || '删除失败，请稍后重试')
  } finally {
    deletingItem.value = null
  }
}
</script>

<style scoped>
.app {
  display: flex;
  min-height: 100vh;
  background-color: #f5f7fa;
}

.content {
  flex: 1;
  padding: 20px;
  overflow-x: hidden;
}

.recommendations {
  padding: 20px;
}

.recommendations-list {
  margin-top: 20px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.recommendation-item {
  transition: transform 0.3s;
}

.recommendation-item:hover {
  transform: translateY(-5px);
}
</style>
