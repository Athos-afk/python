# Questão 7 - Temperaturas da Semana

temperaturas = [28, 30, 27, 31, 29, 32, 26]

soma_temp = 0

print("--- Temperaturas Registradas ---")
for temp in temperaturas:
    print(f"{temp}°C")
    soma_temp += temp

media_temp = soma_temp / len(temperaturas)
maior_temp = max(temperaturas)
menor_temp = min(temperaturas)

dias_acima_da_media = 0
for temp in temperaturas:
    if temp > media_temp:
        dias_acima_da_media += 1

print(f"\nTemperatura média: {media_temp:.2f}°C")
print(f"Maior temperatura: {maior_temp}°C")
print(f"Menor temperatura: {menor_temp}°C")
print(f"Quantidade de dias acima da média: {dias_acima_da_media}")