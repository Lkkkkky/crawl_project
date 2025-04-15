<template>
    <div class="favorite-list">
        <div class="floating-title">
            <el-card class="title-card" shadow="hover">
                <h1>我的收藏</h1>
            </el-card>
        </div>

        <el-card v-if="loading" class="loading-card">
            <el-skeleton :rows="5" animated />
        </el-card>

        <el-card v-else-if="favoriteList.length > 0" class="table-card">
            <el-table :data="favoriteList" stripe style="width: 100%" border>
                <el-table-column type="index" label="序号" width="70" align="center" />
                <el-table-column prop="good_name" label="商品名称" min-width="300" />
                <el-table-column prop="good_price" label="商品价格" width="120" />
                <el-table-column label="商品链接" width="100">
                    <template #default="scope">
                        <el-button type="primary" link @click="handleViewDetail(scope.row)">
                            查看详情
                        </el-button>
                    </template>
                </el-table-column>
                <el-table-column prop="good_source" label="来源平台" width="120" />
                <el-table-column label="操作" width="120" align="center">
                    <template #default="scope">
                        <el-button type="danger" size="small" @click="handleRemoveFavorite(scope.row)">
                            取消收藏
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-card>

        <el-empty v-else description="暂无收藏" />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { ElMessage } from 'element-plus'

const favoriteList = ref([])
const loading = ref(false)

// 获取收藏列表
const getFavoriteList = async () => {
    loading.value = true
    try {
        const response = await axios.get('/api/favorites/list')
        favoriteList.value = response.data
    } catch (error) {
        console.error('获取收藏列表失败:', error)
        ElMessage.error('获取收藏列表失败，请稍后重试')
    } finally {
        loading.value = false
    }
}

// 处理查看详情
const handleViewDetail = async (goods) => {
    try {
        await axios.post('/api/browse/add', {
            good_url: goods.good_url,
            good_name: goods.good_name,
            good_price: goods.good_price,
            good_source: goods.good_source
        })
        window.open(goods.good_url, '_blank')
    } catch (error) {
        console.error('记录浏览历史失败:', error)
    }
}

// 处理取消收藏
const handleRemoveFavorite = async (goods) => {
    try {
        await axios.delete('/api/favorites/remove', {
            params: { goodUrl: goods.good_url }
        })
        ElMessage.success('取消收藏成功')
        // 重新获取收藏列表
        getFavoriteList()
    } catch (error) {
        console.error('取消收藏失败:', error)
        ElMessage.error('取消收藏失败，请稍后重试')
    }
}

// 组件挂载时获取收藏列表
onMounted(() => {
    getFavoriteList()
})
</script>

<style scoped>
.favorite-list {
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
}

.floating-title {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 1000;
    width: 300px;
}

.title-card {
    text-align: center;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(5px);
}

.title-card h1 {
    margin: 0;
    font-size: 24px;
    color: #409EFF;
}

.table-card {
    margin-top: 80px;
}

.loading-card {
    margin-top: 80px;
    padding: 20px;
}
</style>