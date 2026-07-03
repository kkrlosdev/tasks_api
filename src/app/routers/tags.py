from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from app.models.tag import Tag
from app.repository.tag_repository import TagRepository
from app.services.tag_service import TagService

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.get("", summary="Obtiene todos los tags disponibles desde la base de datos.")
def get_tags():
    with TagRepository() as repo:
        service = TagService(repo)
        return service.get_tags()


@router.get("/{id}", summary="Obtiene el tag del ID pasado como parámetro.")
def get_tag_by_id(id: int):
    with TagRepository() as repo:
        service = TagService(repo)
        return service.get_tag_by_id(id)


@router.post("", summary="Crea un tag: restricciones definidas en el modelo Tag.")
def create_tag(tag: Tag):
    with TagRepository() as repo:
        service = TagService(repo)
        created_tag = service.create_tag(tag.name)
        return JSONResponse(
            content=created_tag, headers={"Location": f"/tags/{created_tag['id']}"}
        )


@router.patch(
    "/{id}", summary="Actualiza el nombre del tag del ID pasado como parámetro."
)
def update_tag(id: int, tag: Tag):
    with TagRepository() as repo:
        service = TagService(repo)
        service.update_tag(id, tag.name)
        return Response(status_code=204)


@router.delete("/{id}", summary="Elimina un tag de la base de datos.")
def delete_tag(id: int):
    with TagRepository() as repo:
        service = TagService(repo)
        service.delete_tag(id)
        return Response(status_code=204)
