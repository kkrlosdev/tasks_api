from typing import Any

from app.repository.base_repository import BaseRepository, ExecuteMode
from app.models.task import Task

class TasksRepository(BaseRepository):
    def get_tasks(self) -> list[Task]:
        query = """SELECT * FROM tasks;"""
        return self._execute_query(query, mode=ExecuteMode.ALL)

    def get_task_by_id(self, id: int) -> dict[str, Any]:
        query = """SELECT * FROM tasks WHERE id = ?;"""
        return self._execute_query(query, params=(id,), mode=ExecuteMode.ONE)

    def get_tasks_by_status(self, status: int) -> list[Task]:
        query = """SELECT * FROM tasks WHERE status = ?"""
        return self._execute_query(query, params=(status,), mode=ExecuteMode.ALL)

    def create_task(
                self,
                name: str,
                begin_date: str,
                end_date: str,
                short_description: str | None,
                long_description: str | None,
                status: int
            ):
        query = """
                INSERT INTO tasks (name, begin_date, end_date, short_description, long_description, status)
                VALUES (?, ?, ?, ?, ?, ?);
                """
        data = self._execute_query(
                                query,
                                params=(
                                    name,
                                    begin_date,
                                    end_date,
                                    short_description,
                                    long_description,
                                    status
                                    )
                                )
        if data["rowcount"] == 1:
            return {"id": data["lastrowid"]}

    def delete_task(self, id: int):
        query = """DELETE FROM tasks WHERE id = ?;"""
        data = self._execute_query(query, (id,))
        return data

    def update_task(
                self,
                id: int,
                name: str,
                begin_date: str,
                end_date: str,
                short_description: str | None,
                long_description: str | None,
                status: int
            ):
        query = """
                UPDATE tasks
                SET name = ?, begin_date = ?, end_date = ?,
                short_description = ?, long_description = ?, status = ?
                WHERE id = ?
                """
        return self._execute_query(
                            query,
                            (
                            name,
                            begin_date,
                            end_date,
                            short_description,
                            long_description,
                            status,
                            id
                            )
                        )