
'''
Quiero contar del 1 al 20 de uno en uno.
¿De cuántas maneras eres capaz de hacerlo?
Crea el código para cada una de ellas.
'''

print("===== METODO 1: FOR =====")
for i in range(1, 21):
    print(i)

print("\n===== METODO 2: WHILE =====")
i = 1
while i <= 20:
    print(i)
    i += 1

print("\n===== METODO 3: RECURSIVIDAD =====")
def contar(n):
    if n > 20:
        return
    print(n)
    contar(n + 1)

contar(1)

print("\n===== METODO 4: LISTA + FOR =====")
numeros = list(range(1, 21))
for n in numeros:
    print(n)

print("\n===== METODO 5: COMPRENSION DE LISTA =====")
[print(i) for i in range(1, 21)]

print("\n===== METODO 6: MAP =====")
list(map(print, range(1, 21)))

print("\n===== METODO 7: GENERADOR =====")
def generador():
    for i in range(1, 21):
        yield i

for numero in generador():
    print(numero)


