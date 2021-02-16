# Create a function that receives a string and represents the name of a Smoothie,
# plus additionals or decrements for that smootie like so:
# Classic,+chocolate,-strawberry and returns and array of strings with the ingredients of a given #smoothie

# print(f"Nosso cardapio é {classic}, {forest_Berry}, {freezie}, {freezie}, {greenie}, {vegan_Delite}, {just_Desserts}")
# print("Olá, bom dia, Qual seria o seu pedido?\n")
# pedido = input()
# print(f"Seu pedido é {pedido}")

# "Classic,+chocolate,-strawberry"

cardapio = {
    "Classic": ["strawberry", "banana", "pineapple", "mango", "peach", "honey", "ice", "yogurt"],
    "Forest Berry": ["strawberry", "raspberry", "blueberry", "honey", "ice", "yogurt"],
    "Freezie": ["blackberry", "blueberry", "black currant", "grape juice", "frozen #yogurt"],
    "Greenie": ["green apple", "kiwi", "lime", "avocado", "spinach", "ice", "apple #juice"],
    "Vegan Delite": ["strawberry", "passion fruit", "pineapple", "mango", "peach", "ice", "soy milk"],
    "Just Desserts": ["banana", "ice cream", "chocolate", "peanut", "cherry"]
}


def fazer(pedido):
    ingredients = pedido.split(",")
    print(ingredients)
    final = []

    for n in ingredients:
        print(n)

        if cardapio.get(n):
            final = cardapio.get(n)
            # print(final)

        if n[0] == '+':
            final.append(n[1:])
            # print(n)
        if n[0] == '-':
            final.remove(n[1:])
            # print(n)

        print(final)


fazer("Classic,+chocolate,-strawberry")
