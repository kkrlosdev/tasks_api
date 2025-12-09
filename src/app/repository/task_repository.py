from .base_repository import BaseRepository

class TasksRepository(BaseRepository):
    def get_tasks(self):
        query = """SELECT * FROM tasks;"""
        return self._execute_query(query, mode="all")

    def get_task_by_id(self, id: int):
        query = """SELECT * FROM tasks WHERE id = ?;"""
        return self._execute_query(query, params=(id,), mode="one")

    def get_tasks_by_status(self, status: int):
        query = """SELECT * FROM tasks WHERE status = ?"""
        return self._execute_query(query, params=(status,), mode="all")