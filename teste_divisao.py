print ("teste calculadora")


num1 = float(input("digite um número:"))
operador = input("digite o operador (+, -, *, /,): ")
num2 = float(input("digite outro número:"))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2 
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro,:não e possivel dividir por zero"
else:
    resultado = "operador invalido."

print("resultado:",resultado)
    


