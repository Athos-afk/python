# Questão 8 - Pesquisa de Números

numeros = []

print("Por favor, digite 10 números inteiros:")
for i in range(10):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

positivos = 0
negativos = 0
zeros = 0

print("\n--- Números Digitados ---")
for num in numeros:
    print(num, end=" ")
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

print("\n\n--- Resultados da Pesquisa ---")
print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de iguais a zero: {zeros}")