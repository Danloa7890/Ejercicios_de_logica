'''
Crea una función que calcule y retorne cuántos días hay entre dos cadenas
de texto que representen fechas. Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
La función recibirá dos String y retornará un Int.
La diferencia en días será absoluta (no importa el orden de las fechas).
Si una de las dos cadenas de texto no representa una fecha correcta se
lanzará una excepción.
'''

from datetime import date

def dias_entre_fechas(fecha1: str, fecha2: str):
    try:
        d1, m1, y1 = map(int, fecha1.split("/"))
        d2, m2, y2 = map(int, fecha2.split("/"))
        f1 = date(y1, m1, d1)
        f2 = date(y2, m2, d2)
        return abs((f2 - f1).days)
    except Exception:
        raise ValueError("Una o ambas fechas no son válidas. Use el formato dd/MM/yyyy")

print(dias_entre_fechas("29/04/2002", "9/01/2026"))


