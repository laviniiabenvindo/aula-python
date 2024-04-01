carros = int(input("Quantos carros você tem?"))
juros = ((carros - 1) * 12.50)

if carros >= 2:
    print(f"Você pagará {juros} por mês")
else:
    print("Você está insento do imposto")