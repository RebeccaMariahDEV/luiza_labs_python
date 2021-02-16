"""
Sua missão aqui é criar uma função que obtenha uma tupla e retorne uma tupla com 3 elementos -
o primeiro, o terceiro e o segundo elemento do último para a matriz fornecida.
"""


def easy_unpack(elements: tuple) -> tuple:
    #Insira seu código aqui
    return elements[0], elements[2], elements[-2]


# Não escreva nada abaixo dessa linha
if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # Estas "afirmações" usando apenas para autoverificação e não são necessárias para autoteste
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Terminou')

