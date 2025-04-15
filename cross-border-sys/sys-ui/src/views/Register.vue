<template>
    <div class="register-container">
        <el-form ref="formRef" :model="form" :rules="rules" label-width="120px" class="register-form">
            <h2>用户注册</h2>
            <el-form-item label="用户名" prop="username">
                <el-input v-model="form.username" />
            </el-form-item>
            <el-form-item label="密码" prop="password">
                <el-input v-model="form.password" type="password" />
            </el-form-item>
            <el-form-item label="确认密码" prop="confirmPassword">
                <el-input v-model="form.confirmPassword" type="password" />
            </el-form-item>
            <el-form-item>
                <el-button type="primary" @click="handleSubmit">注册</el-button>
                <el-button @click="$router.push('/login')">返回登录</el-button>
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
    password: '',
    confirmPassword: ''
})

const validatePass = (rule, value, callback) => {
    if (value === '') {
        callback(new Error('请输入确认密码'))
    } else if (value !== form.password) {
        callback(new Error('两次输入密码不一致!'))
    } else {
        callback()
    }
}

const rules = {
    username: [
        { required: true, message: '请输入用户名', trigger: 'blur' },
        { min: 3, max: 20, message: '长度在 3 到 20 个字符', trigger: 'blur' }
    ],
    password: [
        { required: true, message: '请输入密码', trigger: 'blur' },
        { min: 6, message: '密码长度不能小于6位', trigger: 'blur' }
    ],
    confirmPassword: [
        { required: true, validator: validatePass, trigger: 'blur' }
    ]
}

const handleSubmit = async () => {
    if (!formRef.value) return

    await formRef.value.validate(async (valid, fields) => {
        if (valid) {
            try {
                const response = await fetch('/api/auth/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username: form.username,
                        password: form.password
                    })
                })

                const data = await response.json()
                if (data.success) {
                    ElMessage.success('注册成功')
                    router.push('/login')
                } else {
                    ElMessage.error(data.message || '注册失败')
                }
            } catch (error) {
                console.error('Registration error:', error)
                ElMessage.error('注册失败，请稍后重试')
            }
        }
    })
}
</script>

<style scoped>
.register-container {
    display: flex;
    justify-content: center;
    padding-top: 50px;
}

.register-form {
    width: 400px;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}
</style>