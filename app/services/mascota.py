from sqlalchemy.orm import Session

from app.core.exceptions import ClienteNoEncontrado, MascotaNoEncontrada
from app.models.mascota import Mascota
from app.repositories import cliente as cliente_repository
from app.repositories import mascota as mascota_repository
from app.schemas.mascota import MascotaCreate, MascotaUpdate


def crear_mascota(db: Session, datos: MascotaCreate) -> Mascota:
    if cliente_repository.obtener_por_dni(db, datos.dni_propietario) is None:
        raise ClienteNoEncontrado(datos.dni_propietario)
    return mascota_repository.crear(db, datos)


def obtener_mascota(db: Session, id_mascota: int) -> Mascota:
    mascota = mascota_repository.obtener_por_id(db, id_mascota)
    if mascota is None:
        raise MascotaNoEncontrada(id_mascota)
    return mascota


def listar_mascotas(db: Session) -> list[Mascota]:
    return mascota_repository.listar(db)


def listar_mascotas_de_cliente(db: Session, dni_cliente: str) -> list[Mascota]:
    if cliente_repository.obtener_por_dni(db, dni_cliente) is None:
        raise ClienteNoEncontrado(dni_cliente)
    return mascota_repository.listar_por_cliente(db, dni_cliente)


def actualizar_mascota(db: Session, id_mascota: int, cambios: MascotaUpdate) -> Mascota:
    mascota = obtener_mascota(db, id_mascota)
    return mascota_repository.actualizar(db, mascota, cambios)


def eliminar_mascota(db: Session, id_mascota: int) -> None:
    mascota = obtener_mascota(db, id_mascota)
    mascota_repository.eliminar(db, mascota)
