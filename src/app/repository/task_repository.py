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

    def create_task(self, name: str, begin_date: str, end_date: str, short_description: str, long_description: str, status: int):
        query = """
                INSERT INTO tasks (name, begin_date, end_date, short_description, long_description, status)
                VALUES (?, ?, ?, ?, ?, ?);
                """
        try:
            data = self._execute_query(query, mode=None, params=(name, begin_date, end_date, short_description, long_description, status))
            if data["rowcount"] == 1:
                return {"id": data["lastrowid"]}
        except Exception:
            raise

    def delete_task(self, id: int):
        query = """DELETE FROM tasks WHERE id = ?;"""
        data = self._execute_query(query, (id,))
        return data