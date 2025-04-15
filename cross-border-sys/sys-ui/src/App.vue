<template>
  <el-container class="layout-container">
    <el-header class="header">
      <div class="header-content">
        <div class="logo">跨境商品系统</div>
        <div class="user-info" v-if="currentUser">
          <span>{{ currentUser.username }}</span>
          <el-button type="text" @click="handleLogout">退出</el-button>
        </div>
      </div>
    </el-header>
    <el-container class="main-container">
      <el-menu :router="true" default-active="/search" class="el-menu-vertical" :collapse="isCollapse">
        <el-menu-item index="/search">
          <el-icon>
            <Search />
          </el-icon>
          <span>搜索商品</span>
        </el-menu-item>
        <el-menu-item index="/history" v-if="currentUser">
          <el-icon>
            <Clock />
          </el-icon>
          <span>浏览记录</span>
        </el-menu-item>
        <el-menu-item index="/favorites" v-if="currentUser">
          <el-icon>
            <Star />
          </el-icon>
          <span>我的收藏</span>
        </el-menu-item>
      </el-menu>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { Search, Clock, Star } from '@element-plus/icons-vue'
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const isCollapse = ref(false)
const currentUser = ref(null)
const router = useRouter()

const loadCurrentUser = async () => {
  try {
    const response = await fetch('/api/auth/current', {
      credentials: 'include'
    })
    if (response.ok) {
      const data = await response.json()
      if (data.success) {
        currentUser.value = data.data
      }
    }
  } catch (error) {
    console.error('Failed to load user:', error)
  }
}

const handleLogout = async () => {
  try {
    const response = await fetch('/api/auth/logout', {
      method: 'POST',
      credentials: 'include'
    })
    if (response.ok) {
      currentUser.value = null
      ElMessage.success('退出成功')
      router.push('/login')
    }
  } catch (error) {
    ElMessage.error('退出失败')
  }
}

onMounted(() => {
  loadCurrentUser()
})
</script>

<style scoped>
.layout-container {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.header {
  background-color: #409EFF;
  color: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12);
  height: 60px;
}

.logo {
  font-size: 20px;
  font-weight: bold;
}

.main-container {
  flex: 1;
  height: calc(100vh - 60px);
}

.el-menu-vertical {
  height: 100%;
  border-right: solid 1px #e6e6e6;
  width: 200px;
  background-color: #fff;
}

.el-main {
  background-color: #f5f7fa;
  overflow-y: auto;
  padding: 20px;
}

/* 响应式布局 */
@media screen and (max-width: 768px) {
  .el-menu-vertical {
    width: 64px;
  }

  .el-menu-vertical:not(.el-menu--collapse) {
    width: 200px;
  }
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 10px;
  color: white;
}

.user-info .el-button {
  color: white;
}
</style>
