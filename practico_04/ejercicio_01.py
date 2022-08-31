"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS PERSONA (
                            IdPersona integer primary key autoincrement, 
                            nombre text, 
                            fechaNacimiento date,
                            dni integer, 
                            altura integer)""")
    con.close()
    pass # Completar

def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    cur.execute("""DROP TABLE PERSONA""")
    cur.close()
    pass # Completar

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
