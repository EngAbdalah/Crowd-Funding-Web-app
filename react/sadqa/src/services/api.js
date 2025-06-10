// src/services/api.js
import axios from 'axios';

const api = axios.create({
    baseURL: process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000/moderations/api',
});

// Add token to headers for all requests
api.interceptors.request.use((config) => {
    //const token = localStorage.getItem('token');
    const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ5NTQxNjQ4LCJpYXQiOjE3NDk1MDU2NDgsImp0aSI6IjQ1YzNhNGEyY2M2NDQ5NmNiZTZhN2VjZDY4YjI0ODJmIiwidXNlcl9pZCI6M30.C-U56UlcAZ3AzwbbOg5YrxNA-o1LZ8xVgA6K0jiymIo";
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default api;