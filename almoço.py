lista = [num for num in range(1, 11)]
print(lista)

lista = [num * 2 for num in range(1, 11)]
print(lista)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [num for num in lista if num % 2 != 0]
print(impares)

impares = [num if num % 2 != 0 else num * 10 for num in lista]
print(impares)