"""
Você recebe um integer positivo. Sua função deve calcular o produto dos digitos excluindo qualquer Zeros.
Por exemplo: O numero dado é 123405. O resultado será 1*2*3*4*5=120 (Não esquece de excluir os Zeros).
"""


def checkio(number: int) -> int:
    # a variavel aqui é o number
    # Insira seu código aqui
    number = str(number)
    soma = 0

    for x in number:
        if x == "0":
            continue

        x = int(x)
        if soma == 0:
            soma = x
        else:
            soma = soma * x

    return soma


# Não escreva nada abaixo dessa linha
if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print('Terminou')
