import type { CreateTaskResponse, Task, TaskPayload, TaskUpdatePayload } from '../types/task'
import { requestJson } from './http'

export async function getTasks(status?: number): Promise<Task[]> {
  const query = typeof status === 'number' ? `?status=${status}` : ''
  const response = await requestJson<unknown>(`/tasks${query}`, { method: 'GET' })

  if (!Array.isArray(response)) {
    return []
  }

  return response as Task[]
}

export async function createTask(payload: TaskPayload): Promise<CreateTaskResponse> {
  return requestJson<CreateTaskResponse>('/tasks', {
    method: 'POST',
    expectedStatus: [200, 201],
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
}

export async function updateTask(id: number, payload: TaskUpdatePayload): Promise<void> {
  await requestJson<null>(`/tasks/${id}`, {
    method: 'PUT',
    expectedStatus: [200, 204],
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
}

export async function deleteTask(id: number): Promise<void> {
  await requestJson<null>(`/tasks/${id}`, {
    method: 'DELETE',
    expectedStatus: [200, 204],
  })
}
