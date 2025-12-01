from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)

    objetivos = relationship("Objetivo", back_populates="usuario")

class Objetivo(Base):
    __tablename__ = "objetivos"

    id  = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable= False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="objetivos")
    tareas = relationship("Tarea", back_populates="objetivo")

class Tarea(Base):
    __tablename__ = "tareas"

    id =  Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(200), nullable=False)
    completada = Column(Boolean, default=False)
    objetivo_id = Column(Integer, ForeignKey("objetivos.id"), nullable=False)

    objetivo = relationship("Objetivo", back_populates="tareas")