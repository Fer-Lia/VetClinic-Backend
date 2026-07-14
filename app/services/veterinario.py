from sqlalchemy.orm import Session

from app.core.exceptions import VeterinarioNoEncontrado
from app.models.veterinario import Veterinario
from app.repositories import veterinario as veterinario_repository
from app.schemas.veterinario import VeterinarioCreate, VeterinarioUpdate


def crear_veterinario(db: Session, datos: VeterinarioCreate) -> Veterinario:
    return veterinario_repository.crear(db, datos)


def obtener_veterinario(db: Session, dni: str) -> Veterinario:
    veterinario = veterinario_repository.obtener_por_dni(db, dni)
    if veterinario is None:
        raise VeterinarioNoEncontrado(dni)
    return veterinario


def listar_veterinarios(db: Session) -> list[Veterinario]:
    return veterinario_repository.listar(db)


def actualizar_veterinario(db: Session, dni: str, cambios: VeterinarioUpdate) -> Veterinario:
    veterinario = obtener_veterinario(db, dni)
    return veterinario_repository.actualizar(db, veterinario, cambios)


def eliminar_veterinario(db: Session, dni: str) -> None:
    veterinario = obtener_veterinario(db, dni)
    veterinario_repository.eliminar(db, veterinario)
