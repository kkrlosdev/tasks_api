import { API_BASE_URL } from '../constants/api'
import type { ValidationErrorResponse } from '../types/task'

type RequestOptions = RequestInit & {
  expectedStatus?: number[]
}

export class ApiError extends Error {
  readonly status: number
  readonly detail: unknown

  constructor(message: string, status: number, detail: unknown) {
    super(message)
    this.name = 'ApiError'
    this.status = status
    this.detail = detail
  }
}

export async function requestJson<T>(path: string, options: RequestOptions = {}): Promise<T> {
  const { expectedStatus, headers, ...requestInit } = options
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...requestInit,
    headers: {
      Accept: 'application/json',
      ...headers,
    },
  })

  const isJsonResponse = response.headers.get('content-type')?.includes('application/json') ?? false
  const responseBody = isJsonResponse ? await response.json() : null

  if (!response.ok) {
    const message =
      extractValidationMessage(responseBody) ||
      (typeof responseBody === 'object' &&
      responseBody !== null &&
      'detail' in responseBody &&
      typeof responseBody.detail === 'string'
        ? responseBody.detail
        : `La solicitud falló con estado ${response.status}.`)

    throw new ApiError(message, response.status, responseBody)
  }

  if (expectedStatus && !expectedStatus.includes(response.status)) {
    throw new ApiError(
      `La API respondió con un estado inesperado: ${response.status}.`,
      response.status,
      responseBody,
    )
  }

  return responseBody as T
}

function extractValidationMessage(value: unknown): string | null {
  if (!value || typeof value !== 'object' || !('detail' in value)) {
    return null
  }

  const detail = (value as ValidationErrorResponse).detail
  if (!Array.isArray(detail) || detail.length === 0) {
    return null
  }

  return detail.map((issue) => issue.msg).join(' ')
}
