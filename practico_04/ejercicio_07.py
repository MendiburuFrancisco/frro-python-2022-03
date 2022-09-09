"""Base de Datos SQL - Uso de múltiples tablas"""

import datetime
import sqlite3

from ejercicio_02 import agregar_persona
from ejercicio_06 import reset_tabla
from ejercicio_04 import buscar_persona


def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla 
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya 
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que 
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""
    con = sqlite3.connect("example.db")
    cur = con.cursor()

    row = buscar_persona(id_persona)
    if row:
        cur.execute("""SELECT * FROM PersonaPeso WHERE PersonaPeso.IdPersona = ?""", (id_persona,))
        fila_persona_peso = cur.fetchone()
        if fila_persona_peso is None:
            cur.execute('''INSERT INTO PersonaPeso(idPersona, fecha, peso) VALUES(?, ?, ?)''',
                        (id_persona, fecha, peso))
            con.commit()
            con.close()
            return cur.lastrowid
        else:
            fila = list(fila_persona_peso)
            fila[1] = datetime.datetime.strptime(fila_persona_peso[1], '%Y-%m-%d %H:%M:%S')
            fila_persona_peso = tuple(fila)
            if fila_persona_peso[1] < fecha:
                cur.execute('''INSERT INTO PersonaPeso(idPersona, fecha, peso) VALUES(?, ?, ?)''',
                            (id_persona, fecha, peso))
                con.commit()
                con.close()
                return cur.lastrowid
            else:
                return False
    else:
        return False
    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
