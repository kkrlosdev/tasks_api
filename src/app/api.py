from fastapi import FastAPI
import uvicorn

app = FastAPI(
    debug=True,
    title="Tasks API",
    summary="Health check de la API.",
    description="Acopla todos los endpoints habilitados para la gestión de tareas"
)

@app.get("/")
async def health_check():
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(
        app=app
    )