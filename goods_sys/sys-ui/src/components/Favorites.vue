<template>
    <div class="favorites">
        <div class="header">
            <h2>我的收藏</h2>
            <div class="header-actions">
                <el-button type="primary" size="small" @click="handleRefresh">
                    <el-icon><Refresh /></el-icon>
                    刷新
                </el-button>
                <el-button type="danger" size="small" @click="handleClearAll" v-if="favoriteList.length > 0">
                    <el-icon><Delete /></el-icon>
                    清空收藏
                </el-button>
            </div>
        </div>

        <el-card v-if="loading" class="loading-card">
            <el-skeleton :rows="5" animated />
        </el-card>

        <template v-else>
            <div class="filter-section">
                <el-input
                    v-model="searchKeyword"
                    placeholder="搜索商品名称"
                    clearable
                    @input="handleFilter"
                    style="width: 300px"
                >
                    <template #prefix>
                        <el-icon><Search /></el-icon>
                    </template>
                </el-input>
                <el-select v-model="platformFilter" placeholder="选择平台" clearable @change="handleFilter" style="width: 200px">
                    <el-option
                        v-for="platform in platforms"
                        :key="platform"
                        :label="platform"
                        :value="platform"
                    />
                </el-select>
                <el-date-picker
                    v-model="dateRange"
                    type="daterange"
                    range-separator="至"
                    start-placeholder="开始日期"
                    end-placeholder="结束日期"
                    @change="handleFilter"
                    style="width: 300px"
                />
            </div>

            <template v-if="favoriteList.length > 0">
                <el-table 
                    :data="filteredList" 
                    stripe 
                    style="width: 100%" 
                    border
                    @selection-change="handleSelectionChange"
                >
                    <el-table-column type="selection" width="55" />
                    <el-table-column type="index" label="序号" width="70" align="center" />
                    <el-table-column prop="good_name" label="商品名称" min-width="300" show-overflow-tooltip>
                        <template #default="scope">
                            <el-tooltip :content="scope.row.good_name" placement="top">
                                <span>{{ scope.row.good_name }}</span>
                            </el-tooltip>
                        </template>
                    </el-table-column>
                    <el-table-column prop="good_price" label="商品价格" width="120" />
                    <el-table-column label="商品链接" width="100">
                        <template #default="scope">
                            <el-button type="primary" link @click="handleViewDetail(scope.row)">
                                查看详情
                            </el-button>
                        </template>
                    </el-table-column>
                    <el-table-column prop="good_source" label="来源平台" width="120" />
                    <el-table-column prop="favorite_time" label="收藏时间" width="180">
                        <template #default="scope">
                            {{ formatDate(scope.row.favorite_time) }}
                        </template>
                    </el-table-column>
                    <el-table-column label="操作" width="120" align="center">
                        <template #default="scope">
                            <el-button type="danger" size="small" @click="handleRemoveFavorite(scope.row)">
                                取消收藏
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table>

                <div v-if="selectedRows.length > 0" class="batch-actions">
                    <el-button type="danger" size="small" @click="handleBatchRemove">
                        批量取消收藏
                    </el-button>
                    <span class="batch-info">已选择 {{ selectedRows.length }} 项</span>
                </div>
            </template>

            <el-empty 
                v-else 
                :description="favoriteList.length === 0 ? '暂无收藏' : '没有符合条件的记录'" 
            />
        </template>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { Search, Refresh, Delete } from '@element-plus/icons-vue'
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'

const favoriteList = ref([])
const loading = ref(false)
const searchKeyword = ref('')
const platformFilter = ref('')
const dateRange = ref(null)
const selectedRows = ref([])

// 获取所有平台列表
const platforms = computed(() => {
    return [...new Set(favoriteList.value.map(item => item.good_source))]
})

// 过滤后的列表
const filteredList = computed(() => {
    return favoriteList.value.filter(item => {
        const matchKeyword = !searchKeyword.value || 
            item.good_name.toLowerCase().includes(searchKeyword.value.toLowerCase())
        const matchPlatform = !platformFilter.value || 
            item.good_source === platformFilter.value
        const matchDate = !dateRange.value || isDateInRange(item.favorite_time)
        return matchKeyword && matchPlatform && matchDate
    })
})

// 检查日期是否在选择的范围内
const isDateInRange = (dateStr) => {
    if (!dateRange.value) return true
    const date = new Date(dateStr)
    return date >= dateRange.value[0] && date <= dateRange.value[1]
}

// 处理表格选择
const handleSelectionChange = (rows) => {
    selectedRows.value = rows
}

// 批量删除
const handleBatchRemove = async () => {
    try {
        await ElMessageBox.confirm(`确定要取消收藏选中的 ${selectedRows.value.length} 条记录吗？`, '警告', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        })
        
        for (const item of selectedRows.value) {
            await axios.delete('/api/favorites/remove', {
                params: { goodUrl: item.good_url }
            })
        }
        ElMessage.success('批量取消收藏成功')
        getFavoriteList()
    } catch (error) {
        if (error !== 'cancel') {
            console.error('批量取消收藏失败:', error)
            ElMessage.error('批量取消收藏失败，请稍后重试')
        }
    }
}

// 刷新列表
const handleRefresh = () => {
    getFavoriteList()
}

// 清空所有
const handleClearAll = async () => {
    try {
        await ElMessageBox.confirm('确定要清空所有收藏记录吗？', '警告', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        })
        await axios.delete('/api/favorites/clear')
        ElMessage.success('清空成功')
        getFavoriteList()
    } catch (error) {
        if (error !== 'cancel') {
            console.error('清空收藏失败:', error)
            ElMessage.error('清空失败，请稍后重试')
        }
    }
}

// 过滤处理
const handleFilter = () => {
    // 过滤逻辑已通过计算属性实现
}

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

const handleRemoveFavorite = async (goods) => {
    try {
        await ElMessageBox.confirm('确定要取消收藏这条记录吗？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        })
        await axios.delete('/api/favorites/remove', {
            params: { goodUrl: goods.good_url }
        })
        ElMessage.success('取消收藏成功')
        getFavoriteList()
    } catch (error) {
        if (error !== 'cancel') {
            console.error('取消收藏失败:', error)
            ElMessage.error('取消收藏失败，请稍后重试')
        }
    }
}

const formatDate = (dateStr) => {
    const date = new Date(dateStr)
    return date.toLocaleString('zh-CN', {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
    })
}

onMounted(() => {
    getFavoriteList()
})
</script>

<style scoped>
.favorites {
    padding: 20px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.header-actions {
    display: flex;
    gap: 10px;
}

.filter-section {
    display: flex;
    gap: 20px;
    margin-bottom: 20px;
}

.batch-actions {
    margin-top: 20px;
    padding: 10px;
    background-color: #f5f7fa;
    border-radius: 4px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.batch-info {
    color: #909399;
    font-size: 14px;
}

h2 {
    margin: 0;
    color: #409EFF;
}

:deep(.el-table) {
    margin-top: 20px;
}
</style>