from sqlite3 import IntegrityError, Error as SQLiteError

from app.exceptions import TagAlreadyExistsError, TagCreationError, NotFoundError
from app.repository.tag_repository import TagRepository

class TagService:
    def __init__(self, repo: TagRepository):
        self.repo = repo

    def create_tag(self, name: str) -> dict[str, int]:
        try:
            return self.repo.create_tag(name)
        except IntegrityError as e:
            raise TagAlreadyExistsError(
                f"Tag '{name}' ya existe en la base de datos."
            ) from e
        except SQLiteError as e:
            raise TagCreationError(
                f"Error de creación en la base de datos."
            ) from e

    def delete_tag(self, id: int):
        tag = self.repo.get_tag_by_id(id)
        if tag is None:
            raise NotFoundError(f"Tag con ID '{id}' no encontrado en la base de datos.")
        return self.repo.delete_tag(id)

    def update_tag(self, id: int, new_name: str) -> dict[str, int | str]:
        tag = self.repo.get_tag_by_id(id)
        if tag is None:
            raise NotFoundError(f"Tag con ID '{id}' no encontrado en la base de datos.")
        try:
            self.repo.update_tag(id, new_name)
            return {"id": id, "name": new_name}
        except IntegrityError as e:
            raise TagAlreadyExistsError(
                f"Tag '{new_name}' ya existe en la base de datos."
            ) from e

    def get_tags(self):
        return self.repo.get_tags()

    def get_tag_by_id(self, id: int) -> dict[str, int | str]:
        tag = self.repo.get_tag_by_id(id)
        if tag is None:
            raise NotFoundError(f"Tag con ID '{id}' no encontrado en la base de datos.")
        return tag