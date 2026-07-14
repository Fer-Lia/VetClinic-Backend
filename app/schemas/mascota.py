from datetime import date

from pydantic import BaseModel


class MascotaBase(BaseModel):
    nombre: str
    especie: str
    raza: str
    fecha_nacimiento: date
    dni_propietario: str


class MascotaCreate(MascotaBase):
    pass


class MascotaUpdate(BaseModel):
    nombre: str | None = None
    especie: str | None = None
    raza: str | None = None
    fecha_nacimiento: date | None = None


class MascotaOut(MascotaBase):
    id_mascota: int

    model_config = {"from_attributes": True}
