```python
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Métodos para acessar os atributos encapsulados
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def apresentar(self):
        print(f"Marca: {self.__marca}")
        print(f"Modelo: {self.__modelo}")
        print(f"Ano: {self.__ano}")


class Carro(Veiculo):
    def abrir_porta(self):
        print("O carro abriu a porta.")

    def apresentar(self):
        print("Tipo: Carro")
        super().apresentar()


class Moto(Veiculo):
    def empinar(self):
        print("A moto está empinando.")

    def apresentar(self):
        print("Tipo: Moto")
        super().apresentar()


# Cadastro dos veículos
carro = Carro("Toyota", "Corolla", 2024)
moto = Moto("Honda", "CB 500", 2023)


# Exibindo os dados
print("=== CARRO ===")
carro.apresentar()
carro.abrir_porta()

print("\n=== MOTO ===")
moto.apresentar()
moto.empinar()


# Polimorfismo
print("\n=== POLIMORFISMO ===")

veiculos = [carro, moto]

for veiculo in veiculos:
    veiculo.apresentar()
```
