letra = input("Digite uma letra e eu te retornarei a posição dela no alfabeto:\n")

letra.upper()

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]


for n in alfabeto:

    if n == letra:
        
        print(n)