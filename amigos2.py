from random import shuffle


amigos = ["Dani", "Mussi", "Becca", "Cacau", "Nescau", "Chewie", "Luke"]
shuffle(amigos)

for index in range(len(amigos)):
    comprar = index
    receber = index+ 1
    try:
        print(f"{amigos[comprar]:>8} --Tirou--> {amigos[receber]}")
    except IndexError:
        print(f"{amigos[comprar]:>8} --Tirou--> {amigos[0]}")