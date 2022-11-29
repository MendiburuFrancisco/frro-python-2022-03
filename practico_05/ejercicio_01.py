"""Base de Datos - Creación de Clase en ORM"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Socio(Base):
    #Cambie User por Socio
    """Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
        - id_socio: entero (clave primaria, auto-incremental, unico)
        - dni: entero (unico)
        - nombre: string (longitud 250)
        - apellido: string (longitud 250)
    """
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    dni = Column(Integer, unique=True)
    nombre = Column(String(250))
    apellido = Column(String(250))

    def __repr__(self):
        return "<Socio(id_socio='%s', dni='%s', nombre='%s', apellido='%s')>" % (
            self.id_socio,
            self.dni,
            self.nombre,
            self.apellido,
        )

    def __eq__(self, other):
        if self.id_socio == other.id_socio:
            if self.apellido == other.apellido:
                if self.nombre == other.nombre:
                    if self.dni == other.dni:
                        return True
        return False

    # Completar

