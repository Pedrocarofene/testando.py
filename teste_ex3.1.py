print("teste 3.1")

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    tipo = "Par"
else:
     tipo = "Impar"


# Verifica se e Positivo ou Negativo

if numero > 0:
     sinal = "positivo"
elif numero < 0:
     sinal = "negativo"
else:
     sinal = "Zero"

print(f"Você digitou um numero {tipo} e {sinal}.")