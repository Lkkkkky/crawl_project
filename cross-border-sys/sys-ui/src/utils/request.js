import { ElMessage } from 'element-plus'
import router from '../router'

export async function request(url, options = {}) {
    const defaultOptions = {
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json'
        }
    }

    const response = await fetch(url, { ...defaultOptions, ...options })

    if (response.status === 401) {
        ElMessage.error('请先登录')
        router.push('/login')
        throw new Error('Unauthorized')
    }

    const data = await response.json()
    if (!data.success) {
        throw new Error(data.message)
    }

    return data.data
} 