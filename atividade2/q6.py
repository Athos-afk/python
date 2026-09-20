# Questão 6 - Produtos e Preços

# Lista de preços fornecida na questão
precos = [25.50, 40.00, 15.75, 80.00, 120.50]

soma_precos = 0
produtos_caros = []

print("--- Lista de Preços ---")

# 1. Percorre cada preço da lista
for preco in precos:
    print(f"R$ {preco:.2f}")
    # Accumula o total
    soma_precos += preco
    
    # Identifica produtos com preço superior a R$ 50,00
    if preco > 50.00:
        produtos_caros.append(preco)

# 2. Cálculos gerais
total_produtos = len(precos)
preco_medio = soma_precos / total_produtos

# 3. Exibição dos resultados
print(f"\nValor total dos produtos: R$ {soma_precos:.2f}")
print(f"Preço médio: R$ {preco_medio:.2f}")

print("\nProdutos com preço superior a R$ 50,00:")
for caro in produtos_caros:
    print(f"- R$ {caro:.2f}")