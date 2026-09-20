# Questão 10 - Sistema de Análise de Dados

numeros = []

print("Por favor, digite 10 números inteiros:")
for i in range(10):
    val = int(input(f"Digite o {i+1}º número: "))
    numeros.append(val)

soma_total = 0
qtd_pares = 0
qtd_impares = 0

for num in numeros:
    soma_total += num
    if num % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

media = soma_total / len(numeros)
maior_valor = max(numeros)
menor_valor = min(numeros)

acima_da_media = []
for num in numeros:
    if num > media:
        acima_da_media.append(num)

print("\n--- Todos os Números ---")
print(f"Armazenados: {numeros}")
print(f"Acima da média: {acima_da_media}")

print("\n===== RELATÓRIO =====")
print(f"Quantidade de números: {len(numeros)}")
print(f"Soma: {soma_total}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior_valor}")
print(f"Menor valor: {menor_valor}")
print(f"Quantidade de pares: {qtd_pares}")
print(f"Quantidade de ímpares: {qtd_impares}")
print("=====================")