from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import NotFoundError


async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(content={"message": str(exc)}, status_code=404)
