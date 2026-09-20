# Questão 2 - Tabuada[cite: 1]

# Solicita um número inteiro ao utilizador[cite: 1]
numero = int(input("Digite um número: "))

print(f"\n--- Tabuada do {numero} ---")
# Estrutura for para calcular a tabuada de 1 a 10[cite: 1]
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")