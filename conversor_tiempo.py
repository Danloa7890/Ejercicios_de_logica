'''
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
'''

def conversor(dias, horas, minutos, segundos):
    return (
        dias * 24 * 60 * 60 * 1000 +
        horas * 60 * 60 * 1000 +
        minutos * 60 * 1000 +
        segundos * 1000
    )

resultado = conversor(1, 2, 3, 4)
print(resultado)

