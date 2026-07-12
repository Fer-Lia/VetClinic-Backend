from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate


def crear(db: Session, cliente: ClienteCreate) -> Cliente:
    nuevo_cliente = Cliente(**cliente.model_dump())
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente


def obtener_por_dni(db: Session, dni: str) -> Cliente | None:
    return db.get(Cliente, dni)


def listar(db: Session) -> list[Cliente]:
    return list(db.execute(select(Cliente)).scalars().all())


def actualizar(db: Session, cliente_db: Cliente, cambios: ClienteUpdate) -> Cliente:
    datos = cambios.model_dump(exclude_unset=True)
    for campo, valor in datos.items():
        setattr(cliente_db, campo, valor)
    db.commit()
    db.refresh(cliente_db)
    return cliente_db


def eliminar(db: Session, cliente_db: Cliente) -> None:
    db.delete(cliente_db)
    db.commit()
