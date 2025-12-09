from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from ..repository.task_repository import TasksRepository
from ..services.tasks_service import TasksService

router = APIRouter(
    prefix="/tasks",
    tags=["Gestión de tareas."],
)

@router.get(
        "",
        summary="Obtiene todas las tareas disponibles, ofrece la oportunidad de filtrar por estado.",
        description="El parámetro 'status' es opcional. Si es un estado inválido se recibe una HTTPException manejada por FastAPI."
        )
async def get_tasks(status: int | None = None):
    with TasksRepository() as repo:
        service = TasksService(repo)
        data = None
        if status is not None:
            try:
                data = service.list_tasks_by_status(status)
            except ValueError as e:
                raise HTTPException(400, detail=f"{e}")
        else:
            data = service.list_tasks()
        return data