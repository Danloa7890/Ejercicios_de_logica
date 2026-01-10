'''
Crea una función que reciba dos array, un booleano y retorne un array
Si el booleano es verdadero buscará y retornará los elementos comunes
de los dos array.
Si el booleano es falso buscará y retornará los elementos no comunes
de los dos array.
No se pueden utilizar operaciones del lenguaje que
lo resuelvan directamente.
'''

def comparar_arrays(arr1, arr2, comunes: bool):
    resultado = []
    for elemento in arr1:
        encontrado = False
        for otro in arr2:
            if elemento == otro:
                encontrado = True
                break

        if comunes and encontrado:
            resultado.append(elemento)
        if not comunes and not encontrado:
            resultado.append(elemento)
    if not comunes:
        for elemento in arr2:
            encontrado = False
            for otro in arr1:
                if elemento == otro:
                    encontrado = True
                    break

            if not encontrado:
                resultado.append(elemento)
    return resultado

a = [1, 2, 3, 5]
b = [3, 4, 5, 6]

print("Comunes:", comparar_arrays(a, b, True))
print("No comunes:", comparar_arrays(a, b, False))