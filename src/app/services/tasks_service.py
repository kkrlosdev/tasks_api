from ..exceptions.exceptions import NotFoundError
from ..repository.task_repository import TasksRepository
from ..utils.validate_date import validate_date

class TasksService:
    def __init__(self, repo: TasksRepository):
        self.repo = repo

    def list_tasks(self):
        return self.repo.get_tasks()

    def get_task(self, id: int):
        task = self.repo.get_task_by_id(id)
        if not task:
            raise NotFoundError("La tarea no existe.")
        return task

    def list_tasks_by_status(self, status: int):
        if status not in (0, 1, 2):
            raise ValueError("Estado inválido.")
        return self.repo.get_tasks_by_status(status)

    def create_task_service(self, name: str, begin_date: str, end_date: str, short_description: str, long_description: str, status: int):
        if not name:
            raise ValueError("La tarea debe tener un nombre")

        if not validate_date(begin_date):
            raise ValueError("La fecha de inicio no es válida.")

        if not validate_date(end_date):
            raise ValueError("La fecha de finalización no es válida.")

        if status not in (0, 1, 2):
            raise ValueError("Estado inválido.")

        try:
            data = self.repo.create_task(name, begin_date, end_date, short_description, long_description, status)
            lastrowid = data.get("id")
            if lastrowid:
                return lastrowid
        except Exception:
            raise

    def delete_task_service(self, id: int):
        try:
            data = self.repo.delete_task(id)
            rowcount = data["rowcount"]
            if rowcount == 0:
                raise NotFoundError("La tarea no existe en la base de datos.")
            return True
        except Exception:
            raise

    def update_task_service(self,  id: int, name: str, begin_date: str, end_date: str, short_description: str, long_description: str, status: int):
        if not validate_date(begin_date):
            raise ValueError("Fecha de inicio inválida.")
        if not validate_date(end_date):
            raise ValueError("Fecha de finalización inválida.")

        if len(short_description) > 100:
            raise ValueError("Longitud de la descripción corta excede los 100 carácteres.")

        if status not in (0, 1, 2):
            raise ValueError("Estado inválido.")

        exists = self.repo.get_task_by_id(id)
        if not exists:
            raise NotFoundError("Tarea no encontrada en la base de datos.")

        return self.repo.update_task(id, name, begin_date, end_date, short_description, long_description, status)