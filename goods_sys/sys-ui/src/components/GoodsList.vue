<template>
    <div class="goods-list">
        <div class="floating-title">
            <el-card class="title-card" shadow="hover">
                <h1>跨境商品搜索系统</h1>
            </el-card>
        </div>

        <div class="search-box">
            <div class="search-filters">
                <el-input v-model="keyword" placeholder="请输入商品名称" @keyup.enter="handleSearch" class="search-input">
                    <template #append>
                        <el-button type="primary" :loading="loading" @click="handleSearch">
                            <el-icon>
                                <Search />
                            </el-icon>
                            {{ loading ? '搜索中' : '搜索' }}
                        </el-button>
                    </template>
                </el-input>
                <el-select v-model="platformFilter" placeholder="选择平台" clearable class="platform-select">
                    <el-option v-for="platform in platforms" :key="platform" :label="platform" :value="platform" />
                </el-select>
            </div>
        </div>

        <el-card v-if="loading" class="loading-card">
            <el-skeleton :rows="5" animated />
        </el-card>

        <el-card v-else-if="goodsList.length > 0" class="table-card">
            <el-table :data="goodsList" stripe style="width: 100%" border>
                <el-table-column type="index" label="序号" width="70" align="center"
                    :index="(index) => (currentPage - 1) * pageSize + index + 1" />
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
                <el-table-column label="收藏" width="80" align="center">
                    <template #default="scope">
                        <el-button :type="scope.row.isFavorite ? 'warning' : 'default'"
                            :icon="scope.row.isFavorite ? 'Star' : 'StarFilled'" circle
                            @click="toggleFavorite(scope.row)" />
                    </template>
                </el-table-column>
            </el-table>

            <div class="pagination">
                <el-pagination v-model:current-page="currentPage" :page-size="pageSize" :total="total"
                    @current-change="handlePageChange" layout="prev, pager, next" background />
            </div>
        </el-card>

        <el-empty v-else description="暂无数据" />
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Search, Star, StarFilled } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'

// 接收父组件传递的属性
const props = defineProps({
    goodsList: {
        type: Array,
        required: true
    },
    total: {
        type: Number,
        required: true
    },
    loading: {
        type: Boolean,
        required: true
    }
})

// 定义事件
const emit = defineEmits(['search', 'update:goodsList'])

const keyword = ref('')
const currentPage = ref(1)
const pageSize = 10
const platformFilter = ref('')
const platforms = ['CJ', 'neobund', 'GlobalSource']

const handleSearch = () => {
    if (!keyword.value.trim()) {
        ElMessage.warning('请输入搜索关键词')
        return
    }
    currentPage.value = 1
    const searchParams = {
        keyword: keyword.value,
        pageNum: currentPage.value,
        pageSize
    }

    if (platformFilter.value) {
        searchParams.platform = platformFilter.value
    }

    emit('search', searchParams)
}

const handlePageChange = (page) => {
    currentPage.value = page
    const searchParams = {
        keyword: keyword.value,
        pageNum: currentPage.value,
        pageSize
    }

    if (platformFilter.value) {
        searchParams.platform = platformFilter.value
    }

    emit('search', searchParams)
}

const handleViewDetail = async (goods) => {
    try {
        await axios.post('/api/browse/add', {
            good_url: goods.good_url,
            good_name: goods.good_name,
            good_price: goods.good_price,
            good_source: goods.good_source
        });
        window.open(goods.good_url, '_blank');
    } catch (error) {
        console.error('记录浏览历史失败:', error);
    }
};

const toggleFavorite = async (goods) => {
    try {
        if (goods.isFavorite) {
            await axios.delete('/api/favorites/remove', {
                params: { goodUrl: goods.good_url }
            });
            ElMessage.success('取消收藏成功');
        } else {
            await axios.post('/api/favorites/add', {
                good_url: goods.good_url,
                good_name: goods.good_name,
                good_price: goods.good_price,
                good_source: goods.good_source
            });
            ElMessage.success('收藏成功');
        }
        goods.isFavorite = !goods.isFavorite;
    } catch (error) {
        console.error('操作收藏失败:', error);
        ElMessage.error('操作失败，请稍后重试');
    }
};

onMounted(async () => {
    if (props.goodsList.length > 0) {
        try {
            const response = await axios.get('/api/favorites/check', {
                params: {
                    goodUrls: props.goodsList.map(item => item.good_url)
                }
            });
            emit('update:goodsList', props.goodsList.map(item => ({
                ...item,
                isFavorite: response.data.includes(item.good_url)
            })));
        } catch (error) {
            console.error('获取收藏状态失败:', error);
        }
    }
});
</script>

<style scoped>
.goods-list {
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

.search-box {
    margin: 80px 0 20px;
    background: white;
    padding: 20px;
}

.search-filters {
    display: flex;
    gap: 16px;
    align-items: center;
}

.search-input {
    flex: 1;
}

.platform-select {
    width: 160px;
}

.table-card {
    margin-top: 20px;
}

.pagination {
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.loading-card {
    margin-top: 20px;
    padding: 20px;
}

:deep(.el-card__body) {
    padding: 20px;
}
</style>