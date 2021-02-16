"""
    Escreva código para fazer uma função que retorne a primeira palavra em um texto.
    Se seu código estiver certo ao rodar a célula vc reverá receber 'Exemplo: Hello' como output
"""


def first_word(text: str) -> str:
    # Insira seu código aqui
    lista = list(text)

    frase = ''
    start = False

    for value in lista:
        letter = value.isalpha()

        if value == "'":
            letter = True

        if letter and not start:
            start = True

        if start:
            if not letter:
                break

            frase += value

    return frase


# Não escreva nada abaixo dessa linha
if __name__ == '__main__':
    print("Examplo:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print('Terminou')
