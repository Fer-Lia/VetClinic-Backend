from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.core.logging import configurar_logging

configurar_logging()

from app.api.v1.cliente import router as cliente_router
from app.api.v1.mascota import router as mascota_router
from app.api.v1.veterinario import router as veterinario_router
from app.core.exception_handlers import (
    cliente_no_encontrado_handler,
    email_duplicado_handler,
    mascota_no_encontrada_handler,
    veterinario_no_encontrado_handler,
)
from app.core.exceptions import (
    ClienteNoEncontrado,
    EmailDuplicado,
    MascotaNoEncontrada,
    VeterinarioNoEncontrado,
)

app = FastAPI(title="VetClinic API")

origenes_permitidos = [
    "http://localhost:5173",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_exception_handler(ClienteNoEncontrado, cliente_no_encontrado_handler)
app.add_exception_handler(EmailDuplicado, email_duplicado_handler)
app.add_exception_handler(MascotaNoEncontrada, mascota_no_encontrada_handler)
app.add_exception_handler(VeterinarioNoEncontrado, veterinario_no_encontrado_handler)

app.include_router(cliente_router)
app.include_router(mascota_router)
app.include_router(veterinario_router)


@app.get("/")
def read_root():
    return {"mensaje": "VetClinic API funcionando"}
