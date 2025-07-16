print ("teste de IMC (Indice de Massa Corporal)") #calculadora 

nome = (input ("digite seu nome: "))
Peso = float(input("digite seu peso (em kg): "))
altura = float(input("digite sua altura (em metros): "))

#Calculo de IMC

imc = Peso / (altura ** 2)

#Exibiçao de resultado
print (f"\n{nome}, seu IMC é: {imc:.2f}")

#classificaçao IMC 

if imc < 18.5:
    print ("Vocè esta abaixo do peso!!")

elif imc <25:
    print("Peso normal")

elif imc <30:
    print("Sobrepeso!!")

else:
    print("Obesidade")