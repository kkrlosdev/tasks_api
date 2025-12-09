from ..repository.task_repository import TasksRepository

class TasksService:
    def __init__(self, repo: TasksRepository):
        self.repo = repo

    def list_tasks(self):
        return self.repo.get_tasks()

    def get_task(self, id: int):
        task = self.repo.get_task_by_id(id)
        if not task:
            raise ValueError("La tarea no existe.")
        return task

    def list_tasks_by_status(self, status: int):
        if status not in (0, 1, 2):
            raise ValueError("Estado inválido.")
        self.repo.get_tasks_by_status(status)