print("Calculadora de desconto")

valor = float(input("Digite o valor do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

#calculo

valor_desconto = (valor * desconto) / 100
valor_final = valor - valor_desconto 

print(f"Desconto: R${valor_desconto:.2f} ")
print(f"valor com desconto: R$ {valor_final:.2f}" )