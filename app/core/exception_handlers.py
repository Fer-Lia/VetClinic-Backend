from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import ClienteNoEncontrado, EmailDuplicado


async def cliente_no_encontrado_handler(request: Request, exc: ClienteNoEncontrado) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def email_duplicado_handler(request: Request, exc: EmailDuplicado) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": str(exc)})
