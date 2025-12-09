from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from ..repository.task_repository import TasksRepository
from ..services.tasks_service import TasksService
from ..models.task import Task

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

@router.post(
    "",
    summary="Crea una tarea en base de datos.",
    description="Se valida el JSON recibido mediante Pydantic"
)
async def create_task(task: Task):
    with TasksRepository() as repo:
        service = TasksService(repo)
        try:
            task = service.create_task_service(
                                    task.name,
                                    task.begin_date,
                                    task.end_date,
                                    task.short_description,
                                    task.long_description,
                                    task.status
                                    )
            return JSONResponse(content={"id": task}, status_code=201, headers={"Location": f"/tasks/{task}"})
        except ValueError as e:
            raise HTTPException(400, detail=str(e))
        except Exception as e:
            raise HTTPException(500, detail=str(e))