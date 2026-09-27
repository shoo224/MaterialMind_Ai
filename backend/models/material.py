from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    material_code: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True
    )
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str | None] = mapped_column(String(100), nullable=True)
    unit: Mapped[str | None] = mapped_column(String(50), nullable=True)
    manufacturer: Mapped[str | None] = mapped_column(String(150), nullable=True)
    supplier: Mapped[str | None] = mapped_column(String(150), nullable=True)
    specification: Mapped[str | None] = mapped_column(Text, nullable=True)