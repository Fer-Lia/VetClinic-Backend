import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ClienteNoEncontrado,
    EmailDuplicado,
    MascotaNoEncontrada,
    VeterinarioNoEncontrado,
)

logger = logging.getLogger(__name__)


async def cliente_no_encontrado_handler(request: Request, exc: ClienteNoEncontrado) -> JSONResponse:
    logger.warning(f"Cliente no encontrado: {exc.dni}")
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def mascota_no_encontrada_handler(request: Request, exc: MascotaNoEncontrada) -> JSONResponse:
    logger.warning(f"Mascota no encontrada: {exc.id_mascota}")
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def veterinario_no_encontrado_handler(request: Request, exc: VeterinarioNoEncontrado) -> JSONResponse:
    logger.warning(f"Veterinario no encontrado: {exc.dni}")
    return JSONResponse(status_code=404, content={"detail": str(exc)})


async def email_duplicado_handler(request: Request, exc: EmailDuplicado) -> JSONResponse:
    logger.warning(f"Email duplicado: {exc.email}")
    return JSONResponse(status_code=409, content={"detail": str(exc)})

