km_percorrido = float(input("Digite quantidade de km percorrido: "))
dias = int(input("Digite a quantidade de dias do aluguel: "))

print(f"Preço a pagar: R${(km_percorrido * 0.15) + (60 * dias)}")