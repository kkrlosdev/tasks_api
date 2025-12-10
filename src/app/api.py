from fastapi import FastAPI
from .routers import tasks
import uvicorn

app = FastAPI(
    title="Tasks API",
    summary="API REST para gestión de tareas.",
    description="Acopla todos los endpoints habilitados para la gestión de tareas."
)

@app.get(
        "/",
        tags=["Health Check"],
        summary="Health check de la API.",
        description="Retorna un mensaje sencillo para indicar que la API está activa."
        )
async def health_check():
    return {"status": "OK"}

app.include_router(tasks.router)

if __name__ == "__main__":
    uvicorn.run(
        app=app
    )