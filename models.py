from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column("nombre", String(50), nullable=False)
    password = Column(String(255), nullable=False)

    objetivos = relationship("Objetivo", back_populates="usuario")

class Objetivo(Base):
    __tablename__ = "objetivos"

    id  = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable= False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    usuario = relationship("Usuario", back_populates="objetivos")
    tareas = relationship("Tarea", back_populates="objetivo")

    def progreso(self):
        if not self.tareas:
            return 0
        completadas = sum(1 for t in self.tareas if t.completada)
        return round(completadas / len(self.tareas) * 100, 2)
    
class Tarea(Base):
    __tablename__ = "tareas"

    id =  Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(200), nullable=False)
    completada = Column(Boolean, default=False)
    objetivo_id = Column(Integer, ForeignKey("objetivos.id"), nullable=False)

    objetivo = relationship("Objetivo", back_populates="tareas")

    def marcar_completada(self):
        self.completada = True

    def desmarcar_completada(self): 
        self.completada = False