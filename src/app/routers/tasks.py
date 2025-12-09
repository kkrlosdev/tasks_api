from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Gestión de tareas."],
)

@router.get("")
async def get_tasks():
    return {"task1": "description", "task2": "description"}