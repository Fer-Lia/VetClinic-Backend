from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.veterinario import Veterinario
from app.schemas.veterinario import VeterinarioCreate, VeterinarioUpdate


def crear(db: Session, veterinario: VeterinarioCreate) -> Veterinario:
    nuevo_veterinario = Veterinario(**veterinario.model_dump())
    db.add(nuevo_veterinario)
    db.commit()
    db.refresh(nuevo_veterinario)
    return nuevo_veterinario


def obtener_por_dni(db: Session, dni: str) -> Veterinario | None:
    return db.get(Veterinario, dni)


def listar(db: Session) -> list[Veterinario]:
    return list(db.execute(select(Veterinario)).scalars().all())


def actualizar(db: Session, veterinario_db: Veterinario, cambios: VeterinarioUpdate) -> Veterinario:
    datos = cambios.model_dump(exclude_unset=True)
    for campo, valor in datos.items():
        setattr(veterinario_db, campo, valor)
    db.commit()
    db.refresh(veterinario_db)
    return veterinario_db


def eliminar(db: Session, veterinario_db: Veterinario) -> None:
    db.delete(veterinario_db)
    db.commit()
