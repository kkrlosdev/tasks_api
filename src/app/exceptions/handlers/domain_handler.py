from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions import DomainError


async def domain_error_handler(request: Request, exc: DomainError):
    return JSONResponse(content={"message": str(exc)}, status_code=exc.status_code)
