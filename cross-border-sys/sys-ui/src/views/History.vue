<template>
    <div class="history-container">
        <h2>浏览记录</h2>
        <el-table :data="historyList" style="width: 100%" v-loading="loading">
            <el-table-column prop="name" label="商品名称" />
            <el-table-column prop="price" label="商品价格" width="120" />
            <el-table-column prop="platform" label="来源平台" width="120" />
            <el-table-column prop="viewTime" label="浏览时间" width="180" />
            <el-table-column label="操作" width="200">
                <template #default="scope">
                    <el-button type="primary" link @click="openLink(scope.row.link)">
                        查看商品
                    </el-button>
                    <el-button type="danger" link @click="removeHistory(scope.row.id)">
                        删除记录
                    </el-button>
                </template>
            </el-table-column>
        </el-table>

        <div class="pagination">
            <el-pagination v-model:current-page="currentPage" v-model:page-size="pageSize" :total="total"
                @current-change="loadHistory" layout="prev, pager, next" />
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage, ElMessageBox } from 'element-plus'

const historyList = ref([])
const loading = ref(false)
const currentPage = ref(1)
const pageSize = ref(10)
const total = ref(0)

const loadHistory = async (page = 1) => {
    loading.value = true
    try {
        const response = await fetch(`/api/history?page=${page}&size=${pageSize.value}`)
        const data = await response.json()
        historyList.value = data.content
        total.value = data.total
    } catch (error) {
        ElMessage.error('加载浏览记录失败')
    } finally {
        loading.value = false
    }
}

const removeHistory = async (id) => {
    try {
        await ElMessageBox.confirm('确定要删除这条浏览记录吗？', '提示', {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning'
        })

        const response = await fetch(`/api/history/${id}`, {
            method: 'DELETE'
        })

        if (response.ok) {
            ElMessage.success('删除成功')
            loadHistory(currentPage.value)
        }
    } catch (error) {
        if (error !== 'cancel') {
            ElMessage.error('删除失败')
        }
    }
}

const openLink = (url) => {
    window.open(url, '_blank')
}

onMounted(() => {
    loadHistory()
})
</script>

<style scoped>
.history-container {
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