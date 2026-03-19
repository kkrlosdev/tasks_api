export interface Task {
  id: number
  name: string
  begin_date: string
  end_date: string
  short_description: string | null
  long_description: string | null
  status: number
}

export interface TaskPayload {
  name: string
  begin_date: string
  end_date: string
  short_description: string | null
  long_description: string | null
  status: number
}

export interface TaskUpdatePayload extends TaskPayload {
  id: number
}

export interface CreateTaskResponse {
  id: number
}

export interface ValidationErrorItem {
  loc: Array<string | number>
  msg: string
  type: string
}

export interface ValidationErrorResponse {
  detail: ValidationErrorItem[]
}
