from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.mascota import MascotaCreate, MascotaOut, MascotaUpdate
from app.services import mascota as mascota_service

router = APIRouter(prefix="/mascotas", tags=["mascotas"])


@router.post("", response_model=MascotaOut, status_code=status.HTTP_201_CREATED)
def crear_mascota(datos: MascotaCreate, db: Session = Depends(get_db)):
    return mascota_service.crear_mascota(db, datos)


@router.get("", response_model=list[MascotaOut])
def listar_mascotas(db: Session = Depends(get_db)):
    return mascota_service.listar_mascotas(db)


@router.get("/{id_mascota}", response_model=MascotaOut)
def obtener_mascota(id_mascota: int, db: Session = Depends(get_db)):
    return mascota_service.obtener_mascota(db, id_mascota)


@router.put("/{id_mascota}", response_model=MascotaOut)
def actualizar_mascota(id_mascota: int, cambios: MascotaUpdate, db: Session = Depends(get_db)):
    return mascota_service.actualizar_mascota(db, id_mascota, cambios)


@router.delete("/{id_mascota}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mascota(id_mascota: int, db: Session = Depends(get_db)):
    mascota_service.eliminar_mascota(db, id_mascota)
