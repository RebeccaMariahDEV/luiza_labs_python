"""
nome = input("Olá, qual o seu nome?\n")

idade = int(input(f"Prazer {nome}, sou o robô Becca, qual a sua idade?\n"))

robo_idade = 107
robo_idade = robo_idade - idade

print(f"Eu sou {robo_idade} anos mais velha que vc")

nome = input("Olá, qual seu nume?\n")
ano = input("Esta em qual ano da escola?\n")

print("Digite suas ultimas notas de matematica")
notas1 = float(input("primeira nota:\n"))
notas2 = float(input("Segunda nota:\n"))
notas3 = float(input("terceira nota:\n"))

resultado = (notas1 + notas2 + notas3) / 3
print(f"Sua media é: {resultado}")

num = int(input("Digite um valor inteiro de 1 a 100:\n"))

if (num % 3) == 0:
    print("Dedezinho")
else:
    print(num)

num = int(input("Digite um valor inteiro de 1 a 100:\n"))

if (num % 5) == 0:
    print("Linda")
else:
    print(num)

num = int(input("Digite um valor inteiro de 1 a 100:\n"))

if (num % 5) == 0 and (num % 3 ) == 0:
    print("Dedezinha linda")
else:
    print(num)

for num in '95876234585':
    num = int(num)

    if num ==4:
        print('sou 2 +2')
    elif num <= 3:
        print("Sou pequeno")
    else:
        if num == 5:
            num += num
            print(f'5 não, sou {num}')
        else:
            print(num)

import random

for sorteio in range(5):
    num_sorte = random.randint(10,50)
    print(num_sorte)

from random import randint


nome = input('Qual o seu nome: ')

print(f'Olá {nome}, pense em um número de 1 a 20.')

for sorteio in range(1,7):
    num = randint(1,20)
    num1 = int(input('Consegue adivinhar? '))

    if num1 == num:
        print(f"Parabéns! Você acertou, número foi {num1}")
        print('FIM!')

    elif num1 > num:
        print('OPS! digitou um número maior')

    else:
        print('OPS! digitou um número menor')



"""
from random import randint

nome = input('Qual o seu nome: ')

print(f'Olá {nome}, pense em um número de 1 a 20.')

for sorteio in range(1, 7):
    num = randint(1, 20)
    num1 = int(input('Consegue adivinhar? '))

    if num1 == num:
        print(f"Parabéns! Você acertou, número foi {num1}")
        print('FIM!')

    elif num1 > num:
        print('OPS! digitou um número maior')

    else:
        print('OPS! digitou um número menor')


