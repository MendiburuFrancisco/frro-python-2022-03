"""Base de Datos SQL - Baja"""

import datetime
import sqlite3

from ejercicio_01 import reset_tabla
from ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la 
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo 
    borro o no."""
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute("""DELETE FROM PERSONA WHERE PERSONA.IdPersona = ?""", (id_persona,))
    if cur.rowcount > 0:
        con.close()
        return True
    else:
        con.close()
        return False
    pass # Completar

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
