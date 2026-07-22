from pydantic import BaseModel, EmailStr


class VeterinarioBase(BaseModel):
    nombre: str
    apellido: str
    especialidad: str
    telefono: str
    email: EmailStr


class VeterinarioCreate(VeterinarioBase):
    dni: str


class VeterinarioUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    especialidad: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None


class VeterinarioOut(VeterinarioBase):
    dni: str

    model_config = {"from_attributes": True}
