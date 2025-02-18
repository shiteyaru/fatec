precolitro = float(input("Digite o preco do litro: R$"))
desempenho = int(input("Digite o desempenho do carro(km/l): "))
distancia = int(input("Digite a distância entre as cidades(km): "))
litros = distancia / desempenho
precototal = precolitro * litros
print(f"Você gastará {litros} litros, e gastará R${precototal}")