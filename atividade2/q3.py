# Questão 3 - Soma dos Números[cite: 1]

soma_total = 0
soma_pares = 0
soma_impares = 0

# Percorre os números de 1 a 50[cite: 1]
for i in range(1, 51):
    soma_total += i
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

# Apresenta os resultados finais[cite: 1]
print("--- Resultados da Soma (1 a 50) ---")
print(f"Soma de todos os números: {soma_total}")
print(f"Soma dos números pares: {soma_pares}")
print(f"Soma dos números ímpares: {soma_impares}")