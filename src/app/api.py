from fastapi import FastAPI
import uvicorn

from app.config.app import SERVICE_NAME, ENVIRONMENT, STARTUP_TIME, API_PORT
from app.routers import tasks, criticities

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
    return {
        "status": "ok",
        "service_name": SERVICE_NAME,
        "environment": ENVIRONMENT,
        "startup_time": STARTUP_TIME
    }

app.include_router(tasks.router)
app.include_router(criticities.router)


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        port=int(API_PORT)
    )