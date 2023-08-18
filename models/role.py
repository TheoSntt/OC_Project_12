from models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    collaborators = relationship("Collaborator", back_populates="role")

    def __repr__(self):
        return f'{self.name}'
