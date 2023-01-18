import { PUBLIC_API_BASE_URL } from '$env/static/public'

const api = (url: string, method: 'POST' | 'GET' | 'PUT' | 'DELETE' = 'GET', body: unknown = {}) => fetch(PUBLIC_API_BASE_URL + "/v1" + url, {
  headers: {
    "Content-Type": "application/json",
  },
  method,
  body: JSON.stringify(body)
}).then(res => res.json())

export default api
