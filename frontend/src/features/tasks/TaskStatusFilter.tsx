import { TASK_FILTER_OPTIONS } from '../../constants/taskStatus'

type TaskStatusFilterProps = {
  value: string
  disabled?: boolean
  onChange: (value: string) => void
}

export function TaskStatusFilter({ value, disabled = false, onChange }: TaskStatusFilterProps) {
  return (
    <div className="status-filter">
      <label className="status-filter__label" htmlFor="task-status-filter">
        Filtrar por estado
      </label>
      <select
        id="task-status-filter"
        className="select status-filter__select"
        value={value}
        disabled={disabled}
        onChange={(event) => onChange(event.target.value)}
      >
        {TASK_FILTER_OPTIONS.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  )
}
