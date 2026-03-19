export function getTaskStatusLabel(status: number): string {
  if (status === 1) {
    return 'Pendiente'
  }

  if (status === 2) {
    return 'Completada'
  }

  return `Estado ${status}`
}

export function getTaskStatusTone(status: number): string {
  if (status === 1) {
    return 'pending'
  }

  if (status === 2) {
    return 'done'
  }

  return 'unknown'
}
