print("teste exercicio 2 python")

num1 = float(input("digite um número: "))
num2 = float(input("digite outro número: "))

#soma dos 2 numeros

soma = num1 + num2
print("Soma", soma)

#media entre os 2 numeros

media = (num1 + num2) / 2
print("Media", media)

if num1 > num2:
    print(f"O Maior número é: {num1}")
elif num2 > num1:
    print(f"O Maior número é: {num2}")
else:
    print("Os números são iguais.")

