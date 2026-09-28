frase = input("Digite uma frase: ")

i = 0
quantidade_letras = 0
quantidade_numeros = 0
quantidade_espacos = 0

while i < len(frase):

    caractere = frase[i]

    if caractere.isalpha():
        quantidade_letras += 1

    elif caractere.isdigit():
        quantidade_numeros += 1

    elif caractere == " ":
        quantidade_espacos += 1

    i += 1


quantidade_caracteres = len(frase)

palavras = frase.split()
quantidade_palavras = len(palavras)


print("\n--- Análise da frase ---")
print(f"Quantidade de caracteres: {quantidade_caracteres}")
print(f"Quantidade de letras: {quantidade_letras}")
print(f"Quantidade de números: {quantidade_numeros}")
print(f"Quantidade de espaços: {quantidade_espacos}")
print(f"Quantidade de palavras: {quantidade_palavras}")
