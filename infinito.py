''' Crie um programa que pede para o usuário adivinhar o numero que ele está pensando.
O usuário pode dar palpites até acertar mas o programa deve seguir as seguintes instruções:
- O número deve ser entre 1 e 80, inclusivos e sorteado aleatóriamente
- O usuário deve receber dicas de acordo com seu palpite:
    - Se o palpite for até +/- 10 diferente do número, o programa deve dizer que o numero é "só um pouquinho maior/menor"
    - Se o palpite do mais que +/- 10 diferente do número, o programa deve dizer que o número é "muito' maior/menor" que o palpite
    - O programa deve dizer em quantas tentativas o usuário acertou.
    Se for 5 ou menos dizer 'parabens', se for 6 ou mais dizer 'finalmente'
    - O programa deve perguntar se o usuário quer jogar de novo e enquanto ele disser que sim o jogo deve continuar.

jogarNovamente = 'sim'

while jogarNovamente == 'sim' or jogarNovamente.startswith('s'):
    print("Olá humanoide, vamos jogar, adivinha em que numero eu estou pensando de 1 a 80")
    print("Acha que consegue acertar?")
    numero = randint(1, 80)
    palpite = ''
    tentarivas = 0

    while palpite != numero:
        palpite = int(input("Em que numero estou pensando?\n"))
        tentarivas += 1

        if palpite <= (numero - 10):
            print("Esse numero é muito baixo, tenta um pouco mais alto")
        elif (numero - 10) < palpite <numero:
            print("Esse numero é um pouco baixo,porem não muito, tenta um tico mais alto")
        elif palpite >= (numero + 10):
            print("Esse numero é muito alto, tente mais baixo")
        elif (numero + 10) > palpite >numero:
            print("Esse numero é um pouco alto, tenta um pouco mais baixo")
        else:
            continue

    if tentarivas < 6:
        print(f"Parabens, eu estava pensando no {numero}, você acertou em {tentarivas} tentativas")
    else:
        print(f"Finalmente, eu estava pensando no numero {numero}, você acertou em {tentarivas} tentativas")

print()
jogarNovamente = input("Quer jogar novamente?\n").lower()

'''
from random import randint



def jogo():
    jogar = "sim"

    while jogar == 'sim' or jogar.startswith('s'):
        print("Olá humanoide, vamos jogar, adivinha em que numero eu estou pensando de 1 a 80")
        print("Acha que consegue acertar?")
        num = randint(1, 80)
        palpite = ''
        tenta = 0

        while palpite != "não" :
            palpite = int(input("Em que numero estou pensando?\n"))
            tenta += 1

            if palpite <= (num - 10):
                print("Esse numero é muito baixo, tenta um pouco mais alto")

            elif (num - 10) < palpite < num:
                print("Esse numero é um pouco baixo,porem não muito, tenta um tico mais alto")

            elif palpite >= (num + 10):
                print("Esse numero é muito alto, tente mais baixo")

            elif (num + 10) > palpite > num:
                print("Esse numero é um pouco alto, tenta um pouco mais baixo")

            else:
                continue

        if tenta < 6:
            print(f"Parabens, eu estava pensando no {num}, você acertou em {tenta} tentativas")
        else:
            print(f"Finalmente, eu estava pensando no numero {num}, você acertou em {tenta} tentativas")

        jogar = input("Quer jogar novamente?\n").lower()


jogo()





