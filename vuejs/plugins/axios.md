```javascript

// src/plugins/axios.js

import axios from 'axios'
import { ref } from 'vue'

// Create a new axios instance
const instance = axios.create({
  baseURL: process.env.VUE_APP_API_URL || 'http://localhost:8000/api/v1',
  timeout: 30000, // adjust timeout as needed
  headers: { 'Content-Type': 'application/json' },
})

// Request interceptor
instance.interceptors.request.use(config => {
  // You can add things here before a request is made
  // For example, set the auth token of the user.

  return config
}, error => {
  // Do something with the error
  return Promise.reject(error)
})

// Response interceptor
instance.interceptors.response.use(response => {
  // Do something with the response data

  return response
}, error => {
  // Do something with the response error

  return Promise.reject(error)
})

export function useAxios() {
  console.log('Setting API ---- ', process.env)
  const loading = ref(false)
  const error = ref(null)

  const request = async options => {
    loading.value = true
    error.value = null
    try {
      const response = await instance(options)
      console.log(response)

      return response
    } catch (err) {
      error.value = err
    } finally {
      loading.value = false
    }
  }

  return { loading, error, request }
}
```
