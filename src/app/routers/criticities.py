from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse

from app.exceptions import CriticityAlreadyExistsError, CriticityCreationError, NotFoundError
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

@router.get(
        "/{id}",
        summary="Consulta una criticidad específica"
        )
def get_criticity_by_id(id: int):
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        try:
            return service.get_criticity_by_id(id)
        except NotFoundError:
            raise HTTPException(400, detail=f"Tarea con ID {id} no encontrada en la base de datos.")

@router.post(
        "",
        summary="Crea una criticidad: restricciones definidas en el modelo Criticity"
        )
def create_criticity(criticity: Criticity):
    with CriticityRepository() as repo:
        try:
            service = CriticityService(repo)
            created_criticity = service.create_criticity(criticity.name)
        except CriticityAlreadyExistsError as e:
            raise HTTPException(409, detail=str(e))
        except CriticityCreationError as e:
            raise HTTPException(500, detail=str(e))
        return JSONResponse(content={"id": created_criticity["id"]}, headers={"Location": f"/criticities/{created_criticity["id"]}"})

@router.delete(
    "/{id}",
    summary="Elimina una criticidad de la base de datos"
)
def delete_criticity(id: int):
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        try:
            service.delete_criticity(id)
            return Response(status_code=204)
        except NotFoundError as e:
            raise HTTPException(404, detail=str(e))
        except Exception as e:
            raise HTTPException(500, detail=str(e))

@router.patch(
    "/{id}",
    summary="Actualiza el nombre de una criticidad"
)
def update_criticity(id: int, criticity: Criticity) -> dict[str, int | str]:
    with CriticityRepository() as repo:
        service = CriticityService(repo)
        try:
            service.update_criticity(id, criticity.name)
            return {"id": id, "name": criticity.name}
        except NotFoundError as e:
            raise HTTPException(404, detail=str(e))
        except CriticityAlreadyExistsError as e:
            raise HTTPException(409, detail=str(e))
        except CriticityCreationError as e:
            raise HTTPException(500, detail=str(e))