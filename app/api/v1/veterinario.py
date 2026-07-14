from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.veterinario import VeterinarioCreate, VeterinarioOut, VeterinarioUpdate
from app.services import veterinario as veterinario_service

router = APIRouter(prefix="/veterinarios", tags=["veterinarios"])


@router.post("", response_model=VeterinarioOut, status_code=status.HTTP_201_CREATED)
def crear_veterinario(datos: VeterinarioCreate, db: Session = Depends(get_db)):
    return veterinario_service.crear_veterinario(db, datos)


@router.get("", response_model=list[VeterinarioOut])
def listar_veterinarios(db: Session = Depends(get_db)):
    return veterinario_service.listar_veterinarios(db)


@router.get("/{dni}", response_model=VeterinarioOut)
def obtener_veterinario(dni: str, db: Session = Depends(get_db)):
    return veterinario_service.obtener_veterinario(db, dni)


@router.put("/{dni}", response_model=VeterinarioOut)
def actualizar_veterinario(dni: str, cambios: VeterinarioUpdate, db: Session = Depends(get_db)):
    return veterinario_service.actualizar_veterinario(db, dni, cambios)


@router.delete("/{dni}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_veterinario(dni: str, db: Session = Depends(get_db)):
    veterinario_service.eliminar_veterinario(db, dni)
