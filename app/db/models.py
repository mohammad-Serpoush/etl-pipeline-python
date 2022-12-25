from uuid import uuid4
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from sqlalchemy import Column, String, Text, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy import event
from typing import Any
import inflect
from sqlalchemy.ext.declarative import as_declarative, declared_attr

p = inflect.engine()


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        return p.plural(cls.__name__.lower())


class Sample(Base):
    __tablename__ = "sample"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    title = Column(String(1024), nullable=True)
