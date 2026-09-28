def contar_palavras(frase):
    frase = frase.lower()
    palavras = frase.split()

    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    return frequencia


frase = input("Digite uma frase: ")

resultado = contar_palavras(frase)

print("\nFrequência das palavras:")

for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")
