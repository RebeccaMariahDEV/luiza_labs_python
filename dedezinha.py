#Exemplo de um fizz buzz só mudou o nome

for n in range(1, 100):
    if (n % 3 == 0) and (n % 5 == 0):
        print("Dedezinha Querida")
    elif n % 5 == 0:
        print("Dedezinha")
    elif n % 3 == 0:
        print('Querida')
    else:
        print(n)

#Lembrando que o codigo lé de cima para baixo
