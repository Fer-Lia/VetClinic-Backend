from fastapi import FastAPI

from app.api.v1.cliente import router as cliente_router
from app.core.exception_handlers import (
    cliente_no_encontrado_handler,
    email_duplicado_handler,
)
from app.core.exceptions import ClienteNoEncontrado, EmailDuplicado

app = FastAPI(title="VetClinic API")

app.add_exception_handler(ClienteNoEncontrado, cliente_no_encontrado_handler)
app.add_exception_handler(EmailDuplicado, email_duplicado_handler)

app.include_router(cliente_router)


@app.get("/")
def read_root():
    return {"mensaje": "VetClinic API funcionando"}
