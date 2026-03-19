export type TaskStatusOption = {
  value: number
  label: string
}

export const TASK_STATUS_OPTIONS: TaskStatusOption[] = [
  { value: 1, label: 'Pendiente' },
  { value: 2, label: 'Completada' },
]

export const TASK_FILTER_OPTIONS: Array<{ value: string; label: string }> = [
  { value: 'all', label: 'Todas' },
  { value: '1', label: 'Pendiente' },
  { value: '2', label: 'Completada' },
]
