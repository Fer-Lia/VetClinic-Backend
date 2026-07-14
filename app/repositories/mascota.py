from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.mascota import Mascota
from app.schemas.mascota import MascotaCreate, MascotaUpdate


def crear(db: Session, mascota: MascotaCreate) -> Mascota:
    nueva_mascota = Mascota(**mascota.model_dump())
    db.add(nueva_mascota)
    db.commit()
    db.refresh(nueva_mascota)
    return nueva_mascota


def obtener_por_id(db: Session, id_mascota: int) -> Mascota | None:
    return db.get(Mascota, id_mascota)


def listar(db: Session) -> list[Mascota]:
    return list(db.execute(select(Mascota)).scalars().all())


def listar_por_cliente(db: Session, dni_cliente: str) -> list[Mascota]:
    return list(
        db.execute(
            select(Mascota).where(Mascota.dni_propietario == dni_cliente)
        ).scalars().all()
    )


def actualizar(db: Session, mascota_db: Mascota, cambios: MascotaUpdate) -> Mascota:
    datos = cambios.model_dump(exclude_unset=True)
    for campo, valor in datos.items():
        setattr(mascota_db, campo, valor)
    db.commit()
    db.refresh(mascota_db)
    return mascota_db


def eliminar(db: Session, mascota_db: Mascota) -> None:
    db.delete(mascota_db)
    db.commit()
