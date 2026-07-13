from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.cliente import ClienteCreate, ClienteOut, ClienteUpdate
from app.services import cliente as cliente_service

router = APIRouter(prefix="/clientes", tags=["clientes"])


@router.post("", response_model=ClienteOut, status_code=status.HTTP_201_CREATED)
def crear_cliente(datos: ClienteCreate, db: Session = Depends(get_db)):
    return cliente_service.crear_cliente(db, datos)


@router.get("", response_model=list[ClienteOut])
def listar_clientes(db: Session = Depends(get_db)):
    return cliente_service.listar_clientes(db)


@router.get("/{dni}", response_model=ClienteOut)
def obtener_cliente(dni: str, db: Session = Depends(get_db)):
    return cliente_service.obtener_cliente(db, dni)


@router.put("/{dni}", response_model=ClienteOut)
def actualizar_cliente(dni: str, cambios: ClienteUpdate, db: Session = Depends(get_db)):
    return cliente_service.actualizar_cliente(db, dni, cambios)


@router.delete("/{dni}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(dni: str, db: Session = Depends(get_db)):
    cliente_service.eliminar_cliente(db, dni)
