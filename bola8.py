"""
Crie uma versão da Bola 8 Mágica
Ela te da respostas a perguntas diretas. Use a criatividade
Quando você fizer uma pergunta o programa tem que buscar
uma resposta aleatória para responder o usuário
o programa deve perguntar se o usuario gostaria de fazer outra pergunta e continuar rodando até que o usuário responda 'nao'
"""
from random import randint


def perguntas():

    novaPergunta = input("Quer fazer uma pergunta?\n")
    while novaPergunta != "não":

        resposta = ["Acho que não", "Possivel", "Talvez", "Não contaria muito com isso"]

        sorteio = randint(0,3)
        if sorteio == 0:
            print(resposta[0])
        elif sorteio == 1:
            print(resposta[1])
        elif sorteio == 2:
            print(resposta[2])
        elif sorteio == 3:
            print(resposta[3])


        novaPergunta = input("Quer fazer outra pergunta? sim ou não? \n")


perguntas()