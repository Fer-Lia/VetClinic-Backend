from sqlalchemy.orm import Session

from app.core.exceptions import ClienteNoEncontrado, EmailDuplicado
from app.models.cliente import Cliente
from app.repositories import cliente as cliente_repository
from app.schemas.cliente import ClienteCreate, ClienteUpdate


def crear_cliente(db: Session, datos: ClienteCreate) -> Cliente:
    if cliente_repository.obtener_por_email(db, datos.email):
        raise EmailDuplicado(datos.email)
    return cliente_repository.crear(db, datos)


def obtener_cliente(db: Session, dni: str) -> Cliente:
    cliente = cliente_repository.obtener_por_dni(db, dni)
    if cliente is None:
        raise ClienteNoEncontrado(dni)
    return cliente


def listar_clientes(db: Session) -> list[Cliente]:
    return cliente_repository.listar(db)


def actualizar_cliente(db: Session, dni: str, cambios: ClienteUpdate) -> Cliente:
    cliente = obtener_cliente(db, dni)

    if cambios.email and cambios.email != cliente.email:
        if cliente_repository.obtener_por_email(db, cambios.email):
            raise EmailDuplicado(cambios.email)

    return cliente_repository.actualizar(db, cliente, cambios)


def eliminar_cliente(db: Session, dni: str) -> None:
    cliente = obtener_cliente(db, dni)
    cliente_repository.eliminar(db, cliente)
