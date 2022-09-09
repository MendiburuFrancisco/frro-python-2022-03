"""Base de Datos SQL - Creación de tablas auxiliares"""

from ejercicio_01 import borrar_tabla, crear_tabla
import sqlite3


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    cur.execute('''CREATE TABLE if not exists PersonaPeso ( 
                idPersona integer,
                fecha date,
                peso integer,
                FOREIGN KEY(idPersona) REFERENCES Persona(idPersona))''')
    con.close()
    pass # Completar


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    cur.execute("""DROP TABLE if exists PersonaPeso""")
    con.close()
    pass # Completar


# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
