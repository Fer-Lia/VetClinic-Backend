from datetime import date

from sqlalchemy import Date, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base_class import Base


class Mascota(Base):
    __tablename__ = "mascotas"

    id_mascota: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    especie: Mapped[str] = mapped_column(String(50))
    raza: Mapped[str] = mapped_column(String(50))
    fecha_nacimiento: Mapped[date] = mapped_column(Date)
    dni_propietario: Mapped[str] = mapped_column(ForeignKey("clientes.dni"))
