from sqlite3 import IntegrityError, Error as SQLiteError

from app.exceptions import NotFoundError, CriticityAlreadyExistsError, CriticityCreationError
from app.repository.criticity_repository import CriticityRepository

class CriticityService:
    def __init__(self, repo: CriticityRepository):
        self.repo = repo

    def get_criticities(self):
        return self.repo.get_criticities()

    def get_criticity_by_id(self, id: int):
        criticity = self.repo.get_criticity_by_id(id)
        if criticity is None:
            raise NotFoundError(f"Criticidad con ID {id} no encontrada en la base de datos.")
        return criticity

    def delete_criticity(self, id: int):
        criticity = self.repo.get_criticity_by_id(id)
        if criticity is None:
            raise NotFoundError(f"Criticidad con ID {id} no encontrada en la base de datos.")
        return self.repo.delete_criticity(id)

    def update_criticity(self, id: int, new_name: str):
        criticity = self.repo.get_criticity_by_id(id)
        if criticity is None:
            raise NotFoundError(f"Criticidad con ID {id} no encontrada en la base de datos.")
        try:
            return self.repo.update_criticity(id, new_name)
        except IntegrityError as e:
            raise CriticityAlreadyExistsError(
                f"La criticidad '{new_name}' ya existe en la base de datos."
            ) from e

    def create_criticity(self, name: str):
        try:
            return self.repo.create_criticity(name)
        except IntegrityError as e:
            raise CriticityAlreadyExistsError(
                f"La criticidad '{name}' ya existe en la base de datos."
            ) from e
        except SQLiteError as e:
            raise CriticityCreationError(
                f"Error de creación en base de datos"
            ) from e