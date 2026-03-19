import { EmptyState } from '../../components/EmptyState'
import { StatusBadge } from '../../components/StatusBadge'
import type { Task } from '../../types/task'

type TaskTableProps = {
  tasks: Task[]
  busyTaskId: number | null
  isLoading: boolean
  onEdit: (task: Task) => void
  onDelete: (task: Task) => void
}

export function TaskTable({ tasks, busyTaskId, isLoading, onEdit, onDelete }: TaskTableProps) {
  if (!isLoading && tasks.length === 0) {
    return (
      <div className="table-wrapper">
        <EmptyState
          title="No hay tareas para mostrar"
          description="Crea una nueva tarea o cambia el filtro para ver otros resultados."
        />
      </div>
    )
  }

  return (
    <div className="table-wrapper">
      <div className="table-scroll">
        <table className="task-table">
          <thead>
            <tr>
              <th>Tarea</th>
              <th>Fechas</th>
              <th>Estado</th>
              <th>Descripción larga</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {tasks.map((task) => {
              const isBusy = busyTaskId === task.id

              return (
                <tr key={task.id}>
                  <td>
                    <p className="task-title">{task.name}</p>
                    <p className="task-copy">
                      {task.short_description || 'Sin descripción corta.'}
                    </p>
                  </td>
                  <td>
                    <p className="task-copy">Inicio: {task.begin_date}</p>
                    <p className="task-copy">Fin: {task.end_date}</p>
                  </td>
                  <td>
                    <StatusBadge status={task.status} />
                  </td>
                  <td>
                    <p className="task-long-copy">
                      {task.long_description || 'Sin descripción adicional.'}
                    </p>
                  </td>
                  <td>
                    <div className="table-actions">
                      <button
                        type="button"
                        className="table-action table-action--edit"
                        disabled={isBusy}
                        onClick={() => onEdit(task)}
                      >
                        Editar
                      </button>
                      <button
                        type="button"
                        className="table-action table-action--delete"
                        disabled={isBusy}
                        onClick={() => onDelete(task)}
                      >
                        {isBusy ? 'Eliminando...' : 'Eliminar'}
                      </button>
                    </div>
                  </td>
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
    </div>
  )
}
