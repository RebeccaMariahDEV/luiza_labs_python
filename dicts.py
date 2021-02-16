deus = {"nome": "Thor", "Filho de": "Odin", "Função":"Deus do trovão"}

del deus["Filho de"]
print(deus)

print(deus.get('nome'))
print(deus.get("estado civil", "nem te conto"))
deus["estado civil"] = "solteiro"

deus.update({"nome":"Loke", "salario": "infinito", "Estado civil": "Solteiro"})
print(deus)

for coisa in deus.items():
    print(coisa)

for key, value in deus.items():
    print(f"{key}: ---> {value}")

valor = deus.fromkeys('teste', 'foi')
print(valor)
# retorna
"""
Estado civil: ---> Solteiro
{'t': 'foi', 'e': 'foi', 's': 'foi'}
"""