"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("""SELECT * FROM PERSONA WHERE PERSONA.IdPersona = ?""", (id_persona,))
    row = cur.fetchall()
    if len(row) == 0:
        con.close()
        return False
    else:
        fila = [1, 2, 3, 4, 5]
        for i in range(5):
            if i != 2:
                fila[i] = row[0][i]
            else:
                fila[i] = datetime.datetime.strptime(row[0][i], '%Y-%m-%d %H:%M:%S')
        row = tuple(fila)
        con.close()
        return row
    pass # https://stackoverflow.com/questions/21829266/how-to-get-the-numbers-of-data-rows-from-sqlite-table-in-python


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
