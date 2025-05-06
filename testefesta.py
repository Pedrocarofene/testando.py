print ("teste para bebidas das festas!!!!")

#lista das bebidas
sucos_disponiveis = ["maçã verde", "laranja","uva","limão","morango","abacaxi"]
outras_bebidas= ["água","refrigerante"]
bebidas_maior= ["vinho"] + sucos_disponiveis + outras_bebidas
bebidas_menor= sucos_disponiveis + outras_bebidas

idade = int(input("Quantos anos você tem?🤔"))

if  idade >= 18:
   print ("você é maior de idade!")    
   print("bebidas dispóniveis!😄fique avontade!!")
   for bebida in bebidas_maior:
      print(f"- {bebida.capitalize()}")
   print("- nenhuma")

   bebida = input("O que você gostaria de beber🤔?").lower()

   if bebida in bebidas_maior:
      print(f"você escolheu {bebida}.Aproveite a festa!!😄")
   elif bebida in ["nenhuma"]:
      print ("tudo bem,aproveite a festa😄!!")
   else:
      print("opção invalida.Você não escolheu nanhum item da lista")

#Lógica para menores
else:
    print ("você e menor de idade!.Não pode consumir bebidas alcoólicas😬")
    print ("mas temos diferentes tipos de bebidas!fique avontade😄")
    for bebida in bebidas_menor:
      print(f"- {bebida.capitalize()}")
    print("- nenhuma")

    bebida = input("O que você gostaria de beber🤔?").lower()
     
    if bebida == "vinho":
       print("você não tem idade para tomar vinho!!")
    elif bebida in bebidas_menor:
       print(f"Você escolheu {bebida}.Aproveite a festa!😄")
    elif bebida in ["nenhuma"]:
       print ("nenhuma?tudo bem.Aproveite a festa!!")
    else:
       print("opção invalida,selecione uma bebida da lista!!")




      
