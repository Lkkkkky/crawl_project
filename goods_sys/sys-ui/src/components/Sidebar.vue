<template>
    <div class="sidebar">
        <h1 class="title">跨境商品搜索系统</h1>
        <div class="user-info" v-if="username">
            <div class="user-details">
                <div class="username">用户：{{ username }}</div>
            </div>
        </div>
        <el-menu class="menu" :default-active="activeMenu" @select="handleSelect">
            <el-menu-item index="search">
                <el-icon>
                    <Search />
                </el-icon>
                <span>商品搜索</span>
            </el-menu-item>
            <el-menu-item index="favorites">
                <el-icon>
                    <Star />
                </el-icon>
                <span>我的收藏</span>
            </el-menu-item>
            <el-menu-item index="history">
                <el-icon>
                    <Clock />
                </el-icon>
                <span>浏览记录</span>
            </el-menu-item>
            <el-menu-item index="recommendations">
                <el-icon>
                    <Promotion />
                </el-icon>
                <span>猜你喜欢</span>
            </el-menu-item>
        </el-menu>
        <div class="author">@jing3</div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { Search, Star, Clock, Promotion } from '@element-plus/icons-vue'

const activeMenu = ref('search')
const username = ref('')

onMounted(() => {
    username.value = localStorage.getItem('username')
})

const emit = defineEmits(['menu-change'])

const handleSelect = (index) => {
    activeMenu.value = index
    emit('menu-change', index)
}
</script>

<style scoped>
.sidebar {
    width: 250px;
    height: 100vh;
    background-color: #fff;
    border-right: 1px solid #dcdfe6;
    position: relative;
}

.title {
    padding: 20px;
    text-align: center;
    color: #409EFF;
    font-size: 20px;
    border-bottom: 1px solid #dcdfe6;
}

.menu {
    border-right: none;
}

.user-info {
    padding: 15px 20px;
    border-bottom: 1px solid #dcdfe6;
}

.username {
    color: #606266;
    font-size: 14px;
    line-height: 1.5;
}

.author {
    position: absolute;
    bottom: 20px;
    left: 0;
    right: 0;
    text-align: center;
    color: #909399;
    font-size: 14px;
    padding: 10px;
}
</style>