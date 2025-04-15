<template>
    <div class="login-container">
        <el-form ref="formRef" :model="form" :rules="rules" label-width="120px" class="login-form">
            <h2>用户登录</h2>
            <el-form-item label="用户名" prop="username">
                <el-input v-model="form.username" />
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="form.password" type="password" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="handleSubmit">登录</el-button>
                <el-button @click="$router.push('/register')">注册</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import { useRouter } from 'vue-router'

const router = useRouter()
const formRef = ref()
const form = reactive({
    username: '',
    password: ''
})

const rules = {
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' }
    ]
}

const handleSubmit = async () => {
    if (!formRef.value) return

    await formRef.value.validate(async (valid, fields) => {
        if (valid) {
            try {
                const response = await fetch('/api/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(form),
                    credentials: 'include'
                })

                if (response.ok) {
                    ElMessage.success('登录成功')
                    router.push('/search')
                } else {
                    ElMessage.error('用户名或密码错误')
                }
            } catch (error) {
                ElMessage.error('登录失败，请稍后重试')
            }
        }
    })
}
</script>

<style scoped>
.login-container {
    display: flex;
    justify-content: center;
    padding-top: 50px;
}

.login-form {
    width: 400px;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}
</style>