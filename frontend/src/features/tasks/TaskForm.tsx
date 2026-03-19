import { type FormEvent, useEffect, useState } from 'react'
import { TASK_STATUS_OPTIONS } from '../../constants/taskStatus'
import type { Task, TaskPayload } from '../../types/task'
import { formatApiDateToInput, formatInputDateToApi, isValidApiDate } from '../../utils/date'
import { getTaskStatusLabel } from '../../utils/status'

type TaskFormProps = {
  activeTask: Task | null
  isSubmitting: boolean
  formError: string | null
  onCancelEdit: () => void
  onSubmit: (payload: TaskPayload, taskId?: number) => Promise<boolean>
}

type TaskFormState = {
  name: string
  beginDate: string
  endDate: string
  shortDescription: string
  longDescription: string
  status: string
}

const INITIAL_STATE: TaskFormState = {
  name: '',
  beginDate: '',
  endDate: '',
  shortDescription: '',
  longDescription: '',
  status: '1',
}

export function TaskForm({
  activeTask,
  isSubmitting,
  formError,
  onCancelEdit,
  onSubmit,
}: TaskFormProps) {
  const [formState, setFormState] = useState<TaskFormState>(INITIAL_STATE)
  const [localError, setLocalError] = useState<string | null>(null)

  useEffect(() => {
    if (!activeTask) {
      setFormState(INITIAL_STATE)
      setLocalError(null)
      return
    }

    setFormState({
      name: activeTask.name,
      beginDate: formatApiDateToInput(activeTask.begin_date),
      endDate: formatApiDateToInput(activeTask.end_date),
      shortDescription: activeTask.short_description ?? '',
      longDescription: activeTask.long_description ?? '',
      status: String(activeTask.status),
    })
    setLocalError(null)
  }, [activeTask])

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    setLocalError(null)

    const beginDate = formatInputDateToApi(formState.beginDate)
    const endDate = formatInputDateToApi(formState.endDate)

    if (!formState.name.trim()) {
      setLocalError('El nombre de la tarea es obligatorio.')
      return
    }

    if (!isValidApiDate(beginDate) || !isValidApiDate(endDate)) {
      setLocalError('Las fechas deben existir y tener formato DD-MM-YYYY.')
      return
    }

    const payload: TaskPayload = {
      name: formState.name.trim(),
      begin_date: beginDate,
      end_date: endDate,
      short_description: formState.shortDescription.trim() || null,
      long_description: formState.longDescription.trim() || null,
      status: Number(formState.status),
    }

    const wasSuccessful = await onSubmit(payload, activeTask?.id)

    if (!activeTask && wasSuccessful) {
      setFormState(INITIAL_STATE)
    }
  }

  function handleChange<Key extends keyof TaskFormState>(key: Key, value: TaskFormState[Key]) {
    setFormState((current) => ({
      ...current,
      [key]: value,
    }))
  }

  const visibleError = localError || formError
  const statusOptions = TASK_STATUS_OPTIONS.some(
    (option) => option.value === Number(formState.status),
  )
    ? TASK_STATUS_OPTIONS
    : [
        ...TASK_STATUS_OPTIONS,
        { value: Number(formState.status), label: getTaskStatusLabel(Number(formState.status)) },
      ]

  return (
    <section className="panel">
      <div className="panel__header">
        <div>
          <h2 className="panel__title">{activeTask ? 'Editar tarea' : 'Nueva tarea'}</h2>
          <p className="panel__subtitle">
            {activeTask
              ? 'Actualiza el contenido y guarda los cambios.'
              : 'Completa el formulario para crear una tarea nueva.'}
          </p>
        </div>
        {activeTask ? (
          <button
            type="button"
            className="button button--secondary"
            disabled={isSubmitting}
            onClick={onCancelEdit}
          >
            Cancelar edición
          </button>
        ) : null}
      </div>

      <form className="task-form" onSubmit={handleSubmit}>
        <div className="field-group">
          <label htmlFor="task-name">Nombre</label>
          <input
            id="task-name"
            className="input"
            value={formState.name}
            disabled={isSubmitting}
            onChange={(event) => handleChange('name', event.target.value)}
            placeholder="Ej. Preparar demo del sprint"
          />
        </div>

        <div className="field-group field-group--split">
          <div className="field-group">
            <label htmlFor="task-begin-date">Fecha de inicio</label>
            <input
              id="task-begin-date"
              type="date"
              className="input"
              value={formState.beginDate}
              disabled={isSubmitting}
              onChange={(event) => handleChange('beginDate', event.target.value)}
            />
            <span className="field-help">Se enviará como DD-MM-YYYY.</span>
          </div>

          <div className="field-group">
            <label htmlFor="task-end-date">Fecha de fin</label>
            <input
              id="task-end-date"
              type="date"
              className="input"
              value={formState.endDate}
              disabled={isSubmitting}
              onChange={(event) => handleChange('endDate', event.target.value)}
            />
            <span className="field-help">Se enviará como DD-MM-YYYY.</span>
          </div>
        </div>

        <div className="field-group">
          <label htmlFor="task-status">Estado</label>
          <select
            id="task-status"
            className="select"
            value={formState.status}
            disabled={isSubmitting}
            onChange={(event) => handleChange('status', event.target.value)}
          >
            {statusOptions.map((option) => (
              <option key={option.value} value={String(option.value)}>
                {option.label}
              </option>
            ))}
          </select>
        </div>

        <div className="field-group">
          <label htmlFor="task-short-description">Descripción corta</label>
          <textarea
            id="task-short-description"
            className="textarea"
            value={formState.shortDescription}
            disabled={isSubmitting}
            onChange={(event) => handleChange('shortDescription', event.target.value)}
            placeholder="Resumen breve para escaneo rápido."
          />
        </div>

        <div className="field-group">
          <label htmlFor="task-long-description">Descripción larga</label>
          <textarea
            id="task-long-description"
            className="textarea"
            value={formState.longDescription}
            disabled={isSubmitting}
            onChange={(event) => handleChange('longDescription', event.target.value)}
            placeholder="Detalles, contexto o notas relevantes."
          />
        </div>

        {visibleError ? <div className="alert alert--error">{visibleError}</div> : null}

        <div className="button-row">
          <button type="submit" className="button button--primary" disabled={isSubmitting}>
            {isSubmitting
              ? activeTask
                ? 'Guardando...'
                : 'Creando...'
              : activeTask
                ? 'Guardar cambios'
                : 'Crear tarea'}
          </button>
          <button
            type="button"
            className="button button--secondary"
            disabled={isSubmitting}
            onClick={() => {
              setFormState(
                activeTask
                  ? {
                      name: activeTask.name,
                      beginDate: formatApiDateToInput(activeTask.begin_date),
                      endDate: formatApiDateToInput(activeTask.end_date),
                      shortDescription: activeTask.short_description ?? '',
                      longDescription: activeTask.long_description ?? '',
                      status: String(activeTask.status),
                    }
                  : INITIAL_STATE,
              )
              setLocalError(null)
            }}
          >
            Limpiar
          </button>
        </div>
      </form>
    </section>
  )
}
