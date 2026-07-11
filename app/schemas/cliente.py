from pydantic import BaseModel, EmailStr


class ClienteBase(BaseModel):
    nombre: str
    apellido: str
    direccion: str
    telefono: str
    email: EmailStr


class ClienteCreate(ClienteBase):
    dni: str


class ClienteUpdate(BaseModel):
    nombre: str | None = None
    apellido: str | None = None
    direccion: str | None = None
    telefono: str | None = None
    email: EmailStr | None = None


class ClienteOut(ClienteBase):
    dni: str

    model_config = {"from_attributes": True}
