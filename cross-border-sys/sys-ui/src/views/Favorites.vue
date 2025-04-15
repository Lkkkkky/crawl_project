<template>
    <div class="favorites-container">
        <h2>我的收藏</h2>
        <el-table :data="favoritesList" style="width: 100%" v-loading="loading">
            <el-table-column prop="name" label="商品名称" />
            <el-table-column prop="price" label="商品价格" width="120" />
            <el-table-column prop="platform" label="来源平台" width="120" />
            <el-table-column prop="collectTime" label="收藏时间" width="180" />
            <el-table-column label="操作" width="200">
                <template #default="scope">
                    <el-button type="primary" link @click="openLink(scope.row.link)">
                        查看商品
                    </el-button>
                    <el-button type="danger" link @click="removeFavorite(scope.row.id)">
                        取消收藏
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <div class="pagination">
            <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :total="total"
                @current-change="loadFavorites" layout="prev, pager, next" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

const favoritesList = ref([])
const loading = ref(false)
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)

const loadFavorites = async (page = 1) => {
    loading.value = true
    try {
        const response = await fetch(`/api/favorites?page=${page}&size=${pageSize.value}`)
        const data = await response.json()
        favoritesList.value = data.content
        total.value = data.total
    } catch (error) {
        ElMessage.error('加载收藏列表失败')
    } finally {
        loading.value = false
    }
}

const removeFavorite = async (id) => {
    try {
        await ElMessageBox.confirm('确定要取消收藏这个商品吗？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        })

        const response = await fetch(`/api/favorites/${id}`, {
            method: 'DELETE'
        })

        if (response.ok) {
            ElMessage.success('取消收藏成功')
            loadFavorites(currentPage.value)
        }
    } catch (error) {
        if (error !== 'cancel') {
            ElMessage.error('取消收藏失败')
        }
    }
}

const openLink = (url) => {
    window.open(url, '_blank')
}

onMounted(() => {
    loadFavorites()
})
</script>

<style scoped>
.favorites-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.el-table {
    flex: 1;
    overflow: auto;
}

.pagination {
    display: flex;
    justify-content: center;
    padding: 20px 0;
}
</style>