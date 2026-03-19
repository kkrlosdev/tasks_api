import { getTaskStatusLabel, getTaskStatusTone } from '../utils/status'

type StatusBadgeProps = {
  status: number
}

export function StatusBadge({ status }: StatusBadgeProps) {
  const tone = getTaskStatusTone(status)

  return (
    <span className={`status-badge status-badge--${tone}`}>
      <span className="status-badge__dot" />
      {getTaskStatusLabel(status)}
    </span>
  )
}
