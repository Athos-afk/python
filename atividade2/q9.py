# Questão 9 - Análise de Vendas

vendas = [15, 22, 18, 30, 25, 20]

total_vendas = 0

print("--- Vendas Diárias ---")
dia = 1
for venda in vendas:
    print(f"Dia {dia}: {venda} produtos")
    total_vendas += venda
    dia += 1

media_vendas = total_vendas / len(vendas)
maior_venda = max(vendas)

dias_acima = []
dia = 1
for venda in vendas:
    if venda > media_vendas:
        dias_acima.append(dia)
    dia += 1

print(f"\nTotal de produtos vendidos: {total_vendas}")
print(f"Média diária de vendas: {media_vendas:.2f}")
print(f"Maior número de vendas registrado: {maior_venda}")
print(f"Dias com vendas acima da média: {dias_acima}")