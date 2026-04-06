from typing import Any

from app.repository.base_repository import BaseRepository, ExecuteMode

class CriticityRepository(BaseRepository):
    def create_criticity(self, name: str) -> dict[str, int] | None:
        query: str = """INSERT INTO criticities (name) VALUES (?);"""
        data = self._execute_query(query, (name,))
        if data["rowcount"] == 1:
            return {"id": data["lastrowid"]}

    def get_criticities(self) -> list[dict[str, Any]]:
        query: str = """SELECT * FROM criticities;"""
        return self._execute_query(query, mode=ExecuteMode.ALL)

    def update_criticity(self, id: int, new_name: str) -> dict[str, int | None]:
        query: str = """
                    UPDATE criticities
                    SET name = ? WHERE id = ?;
                    """
        return self._execute_query(query, (new_name, id))

    def delete_criticity(self, id: int) -> dict[str, int | None]:
        query: str = """DELETE FROM criticities WHERE id = ?;"""
        return self._execute_query(query, (id,))