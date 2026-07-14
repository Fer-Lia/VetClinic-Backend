from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Veterinario(Base):
    __tablename__ = "veterinarios"

    dni: Mapped[str] = mapped_column(String(20), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    especialidad: Mapped[str] = mapped_column(String(100))
    telefono: Mapped[str] = mapped_column(String(20))
