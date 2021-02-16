from random import choice, randint

"""def amigos():
    amigosHP = ["Hermione", "Harry ", "Ronald", "Rúbeo", "Dobby"]
    choice(amigosHP)
    for n in amigosHP:
        print(n)
        secreto = []
        
        secreto.append(n)

    print(secreto)




amigos()"""

hp = ["Hermione", "Harry ", "Ronald", "Rúbeo", "Dobby"]
sorteado = []
i = 0

while len(sorteado) < len(hp): #a lista de sorteado for menor que a lista de hp ele vai continuar
    a = choice(hp)
    if(hp[i] != a) and (hp[i] != a): #a é a lista de sorteio de nome, se o sorteio do nome for igual ao a sortei outro
        print(f"{hp[i]} saiu com a {a}")
        sorteado.append(a)
        i += 1 # vai representar o index da lista hp, o +=1 moda o valor do index no loop, assim ele pega outro index e adiciona na lista sorteado
        #assim quando a lista sorteado foi maior que len o while para
    else:
        continue