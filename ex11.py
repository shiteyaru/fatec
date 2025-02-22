peso = float(input("Digite o peso em gramas do saco de ração: "))
quant = float(input("Digite a quantidade de ração para cada gato: "))
resto = peso - (quant * 10)
print(f"Restará {resto} gramas no saco de ração")