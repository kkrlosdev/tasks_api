from app.repository.criticity_repository import CriticityRepository

class CriticityService:
    def __init__(self, repo: CriticityRepository):
        self.repo = repo

    def get_criticities(self):
        return self.repo.get_criticities()

    def delete_criticity(self, id: int):
        return self.repo.delete_criticity(id)

    def update_criticity(self, id: int, new_name: str):
        return self.repo.update_criticity(id, new_name)

    def create_criticity(self, name: str):
        return self.repo.create_criticity(name)