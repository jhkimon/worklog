import axios from 'axios';

// Axios 인스턴스 생성
const API = axios.create({
    baseURL: 'http://localhost:8000', // Django 서버의 기본 URL
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken(),
    },
});

function getCSRFToken() {
    const cookieValue = document.cookie
        .split('; ')
        .find((cookie) => cookie.startsWith('csrftoken='))
        .split('=')[1];
    return cookieValue;
}

// Axios 요청 전에 회원 / 비회원 확인
API.interceptors.request.use(
    async (config) => {
        // 회원 로직
        const token = localStorage.getItem('authToken');
        if (token) {
            config.headers['Authorization'] = `Token ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default API;
