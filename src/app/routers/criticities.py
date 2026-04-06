from fastapi import APIRouter

from app.models.criticity import Criticity
from app.repository.criticity_repository import CriticityRepository
from app.services.criticity_service import CriticityService

router = APIRouter(
    prefix="/criticities",
    tags=["Criticidades"]
)

@router.get(
        "",
        summary="Consulta todas las criticidades"
        )
def get_criticities():
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        return service.get_criticities()

@router.post(
        "",
        summary="Crea una criticidad: restricciones definidas en el modelo Criticity"
        )
def create_criticity(criticity: Criticity):
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        return service.create_criticity(criticity.name)

@router.delete(
    "/{id}",
    summary="Elimina una criticidad de la base de datos"
)
def delete_criticity(id: int):
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        return service.delete_criticity(id)

@router.patch(
    "/{id}",
    summary="Actualiza el nombre de una criticidad"
)
def update_criticity(id: int, criticity: Criticity):
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        return service.update_criticity(id, criticity.name)