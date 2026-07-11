from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Cliente(Base):
    __tablename__ = "clientes"

    dni: Mapped[str] = mapped_column(String(20), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    apellido: Mapped[str] = mapped_column(String(100))
    direccion: Mapped[str] = mapped_column(String(200))
    telefono: Mapped[str] = mapped_column(String(20))
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
