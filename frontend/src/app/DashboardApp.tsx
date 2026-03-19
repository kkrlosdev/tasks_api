import { TaskDashboard } from '../features/tasks/TaskDashboard'

export function DashboardApp() {
  return (
    <main className="app-shell">
      <div className="app-shell__content">
        <TaskDashboard />
      </div>
    </main>
  )
}
