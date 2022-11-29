"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        engine = create_engine("sqlite:///:memory:", echo=True)
        self.Session = sessionmaker(engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        pass # Completar

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        with self.Session() as session:
            s = session.query(Socio).filter(Socio.id_socio == id_socio).one()
            return s
        pass # Completar

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        with self.Session() as session:
            return session.query(Socio).filter(Socio.dni == dni_socio).one()
        pass # Completar
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        with self.Session() as session:
            cosa = session.query(Socio).all()
        return cosa
        pass # Completar

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        session = self.Session()
        session.begin()
        try:
            session.query(Socio).delete()
        except:
            session.rollback()
            return False
        else:
            session.commit()
            session.close()
            return True
        pass # Completar

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        with self.Session() as session:
            session.begin()
            try:
                session.add(socio)
            except:
                session.rollback()
                raise
            else:
                session.commit()
                return self.buscar(socio.id_socio)
        pass # Completar

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado
        fue exitoso.
        """
        with self.Session() as session:
            session.begin()
            try:
                borrar = self.buscar(id_socio)
                session.delete(borrar)
            except:
                session.rollback()
                return False
            else:
                session.commit()
                session.close()
                return True
        pass # Completar

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        with self.Session() as session:
            session.begin()
            try:
                session.query(Socio).filter(Socio.id_socio == socio.id_socio).update({
                    'dni': socio.dni,
                    'nombre': socio.nombre,
                    'apellido': socio.apellido,
                })
            except:
                session.rollback()
                raise
            else:
                session.commit()
                return self.buscar(socio.id_socio)
        pass # Completar
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        with self.Session() as session:
            session.begin()
            try:
                return session.query(Socio).count()
            except:
                session.rollback()
                raise
        pass # Completar



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
print(socio)
assert socio.id_socio > 0

# Test Baja
assert datos.baja(socio.id_socio) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id_socio)
assert socio_3_modificado.id_socio == socio_3.id_socio
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN