<template>
    <div class="search-container">
        <el-input v-model="searchQuery" placeholder="请输入商品名称" clearable @input="handleSearch" class="search-input">
            <template #prefix>
                <el-icon>
                    <Search />
                </el-icon>
            </template>
        </el-input>

        <el-table :data="products" style="width: 100%" v-loading="loading">
            <el-table-column prop="name" label="商品名称" />
            <el-table-column prop="price" label="商品价格" width="120" />
            <el-table-column prop="platform" label="来源平台" width="120" />
            <el-table-column label="操作" width="200">
                <template #default="scope">
                    <el-button type="primary" link @click="openLink(scope.row.link)">
                        查看商品
                    </el-button>
                    <el-button type="success" link @click="addToFavorites(scope.row)">
                        收藏
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <div class="pagination">
            <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :total="total"
                @current-change="handlePageChange" layout="prev, pager, next" />
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

const searchQuery = ref('')
const products = ref([])
const loading = ref(false)
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)

const handleSearch = async () => {
    if (searchQuery.value.trim() === '') {
        return
    }

    loading.value = true
    try {
        // 这里需要调用后端API
        const response = await fetch(`/api/products/search?query=${searchQuery.value}&page=${currentPage.value}&size=${pageSize.value}`)
        const data = await response.json()
        products.value = data.content
        total.value = data.total
    } catch (error) {
        ElMessage.error('搜索失败，请稍后重试')
    } finally {
        loading.value = false
    }
}

const handlePageChange = (page) => {
    currentPage.value = page
    handleSearch()
}

const openLink = (url) => {
    window.open(url, '_blank')
}

const addToFavorites = async (product) => {
    try {
        const response = await fetch('/api/favorites', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(product)
        })

        if (response.ok) {
            ElMessage.success('收藏成功')
        } else {
            ElMessage.error('收藏失败')
        }
    } catch (error) {
        ElMessage.error('收藏失败，请稍后重试')
    }
}
</script>

<style scoped>
.search-container {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.search-input {
    width: 100%;
    max-width: 600px;
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

/* 响应式布局 */
@media screen and (max-width: 768px) {
    .search-container {
        gap: 10px;
    }

    .search-input {
        max-width: 100%;
    }
}
</style>