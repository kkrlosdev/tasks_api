from app.repository.base_repository import BaseRepository, ExecuteMode

class TagRepository(BaseRepository):
    def create_tag(self, name: str) -> dict[str, int]:
        query = """INSERT INTO tags (name) VALUES (?);"""
        data = self._execute_query(query, (name,))
        return {"id": data["lastrowid"]}

    def delete_tag(self, id: int):
        query = """DELETE FROM tags WHERE id = ?;"""
        return self._execute_query(query, (id,))

    def update_tag(self, id: int, new_name: str):
        query = """UPDATE tags SET name = ? WHERE id = ?;"""
        return self._execute_query(query, (new_name, id))

    def get_tags(self) -> list[dict[str, int | str]]:
        query = """SELECT * FROM tags"""
        return self._execute_query(query, mode=ExecuteMode.ALL)

    def get_tag_by_id(self, id: int) -> dict[str, int | str] | None:
        query = """SELECT * FROM tags WHERE id = ?;"""
        return self._execute_query(query, (id,), mode=ExecuteMode.ONE)