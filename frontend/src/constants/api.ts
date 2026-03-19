export const DEFAULT_API_BASE_URL = import.meta.env.DEV ? '/api' : 'http://192.168.40.8:8000'

export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL?.trim() || DEFAULT_API_BASE_URL
