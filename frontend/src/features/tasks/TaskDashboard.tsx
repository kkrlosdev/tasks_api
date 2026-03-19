import { useEffect, useState } from 'react'
import { API_BASE_URL } from '../../constants/api'
import type { Task, TaskPayload, TaskUpdatePayload } from '../../types/task'
import { getErrorMessage } from '../../utils/error'
import { createTask, deleteTask, getTasks, updateTask } from '../../services/tasksApi'
import { TaskForm } from './TaskForm'
import { TaskStatusFilter } from './TaskStatusFilter'
import { TaskTable } from './TaskTable'

export function TaskDashboard() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [selectedStatus, setSelectedStatus] = useState<string>('all')
  const [activeTask, setActiveTask] = useState<Task | null>(null)
  const [isLoading, setIsLoading] = useState<boolean>(true)
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false)
  const [busyTaskId, setBusyTaskId] = useState<number | null>(null)
  const [screenError, setScreenError] = useState<string | null>(null)
  const [formError, setFormError] = useState<string | null>(null)

  useEffect(() => {
    void loadTasks(selectedStatus)
  }, [selectedStatus])

  async function loadTasks(statusFilter: string) {
    setIsLoading(true)
    setScreenError(null)

    try {
      const status = statusFilter === 'all' ? undefined : Number(statusFilter)
      const data = await getTasks(status)
      setTasks(data)
    } catch (error) {
      setScreenError(getErrorMessage(error))
    } finally {
      setIsLoading(false)
    }
  }

  async function handleSubmit(payload: TaskPayload, taskId?: number): Promise<boolean> {
    setIsSubmitting(true)
    setFormError(null)

    try {
      if (typeof taskId === 'number') {
        const updatePayload: TaskUpdatePayload = { ...payload, id: taskId }
        await updateTask(taskId, updatePayload)
        setActiveTask(null)
      } else {
        await createTask(payload)
      }

      await loadTasks(selectedStatus)
      return true
    } catch (error) {
      setFormError(getErrorMessage(error))
      return false
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleDelete(task: Task) {
    const confirmed = window.confirm(`¿Eliminar la tarea "${task.name}"?`)
    if (!confirmed) {
      return
    }

    setBusyTaskId(task.id)
    setScreenError(null)

    try {
      await deleteTask(task.id)
      if (activeTask?.id === task.id) {
        setActiveTask(null)
      }
      await loadTasks(selectedStatus)
    } catch (error) {
      setScreenError(getErrorMessage(error))
    } finally {
      setBusyTaskId(null)
    }
  }

  const totalTasks = tasks.length
  const completedTasks = tasks.filter((task) => task.status === 2).length
  const visibleState = isLoading
    ? 'Cargando tareas desde la API'
    : screenError
      ? 'Con inconvenientes de conexión'
      : 'Sincronizado con la API'

  return (
    <>
      <section className="hero">
        <article className="hero__card">
          <span className="eyebrow">Tasks Dashboard v0.1.0</span>
          <h1>Gestiona tareas con una vista clara y lista para operar.</h1>
          <p>
            Crea, filtra, actualiza y elimina tareas en una sola pantalla, con una
            interfaz enfocada en velocidad, legibilidad y mantenimiento.
          </p>
        </article>

        <div className="hero__summary">
          <article className="metric-card">
            <p className="metric-card__label">Tareas visibles</p>
            <p className="metric-card__value">{isLoading ? '...' : totalTasks}</p>
            <p className="metric-card__caption">Filtro activo: {getFilterLabel(selectedStatus)}</p>
          </article>

          <article className="metric-card">
            <p className="metric-card__label">Completadas</p>
            <p className="metric-card__value">{isLoading ? '...' : completedTasks}</p>
            <p className="metric-card__caption">API base: {API_BASE_URL}</p>
          </article>
        </div>
      </section>

      <div className="topbar">
        <div className="status-line">
          <span
            className={`status-line__dot${screenError ? ' status-line__dot--error' : ''}`}
          />
          <span>{visibleState}</span>
        </div>
        <button
          type="button"
          className="button button--secondary"
          disabled={isLoading || isSubmitting}
          onClick={() => void loadTasks(selectedStatus)}
        >
          {isLoading ? 'Actualizando...' : 'Recargar'}
        </button>
      </div>

      <div className="dashboard-grid">
        <TaskForm
          activeTask={activeTask}
          isSubmitting={isSubmitting}
          formError={formError}
          onCancelEdit={() => {
            setActiveTask(null)
            setFormError(null)
          }}
          onSubmit={handleSubmit}
        />

        <section className="panel">
          <div className="tasks-header">
            <div>
              <h2 className="panel__title">Tabla de tareas</h2>
              <p className="panel__subtitle">
                Revisa el estado actual y usa las acciones por fila para editar o eliminar.
              </p>
            </div>
            <TaskStatusFilter
              value={selectedStatus}
              disabled={isLoading || isSubmitting}
              onChange={setSelectedStatus}
            />
          </div>

          {screenError ? <div className="alert alert--error">{screenError}</div> : null}
          {!screenError && isLoading ? (
            <div className="alert alert--info">Cargando tareas y sincronizando la vista...</div>
          ) : null}

          <TaskTable
            tasks={tasks}
            busyTaskId={busyTaskId}
            isLoading={isLoading}
            onEdit={(task) => {
              setActiveTask(task)
              setFormError(null)
              window.scrollTo({ top: 0, behavior: 'smooth' })
            }}
            onDelete={(task) => void handleDelete(task)}
          />
        </section>
      </div>
    </>
  )
}

function getFilterLabel(value: string): string {
  if (value === '1') {
    return 'Pendiente'
  }

  if (value === '2') {
    return 'Completada'
  }

  return 'Todas'
}
