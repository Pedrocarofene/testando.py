print("🎉 Bem-vindo à festa! 🎉")

# Bebidas disponíveis
sucos_disponiveis = ["laranja", "uva", "abacaxi"]
outras_bebidas = ["refrigerante", "água"]
bebidas_maior = ["vinho"] + sucos_disponiveis + outras_bebidas
bebidas_menor = sucos_disponiveis + outras_bebidas

# Entrada de idade
idade = int(input("Quantos anos você tem? "))

# Lógica para maiores de idade
if idade >= 18:
    print("Você é maior de idade.")
    print("Bebidas disponíveis:")
    for bebida in bebidas_maior:
        print(f" - {bebida.capitalize()}")
    print(" - Nenhuma")

    bebida = input("O que você gostaria de beber? ").lower()

    if bebida in bebidas_maior:
        print(f"\nVocê escolheu {bebida}. Aproveite a festa!")
    elif bebida in ["nenhuma", "não quero", "nao quero"]:
        print("\nTudo bem, você não quis nenhuma bebida. Aproveite a festa!")
    else:
        print("\nOpção inválida. Você não escolheu uma bebida da lista.")

# Lógica para menores de idade
else:
    print("\nVocê é menor de idade. Não pode consumir bebidas alcoólicas.")
    print("Bebidas disponíveis:")
    for bebida in bebidas_menor:
        print(f" - {bebida.capitalize()}")
    print(" - Nenhuma")

    bebida = input("O que você gostaria de beber? ").lower()

    if bebida == "vinho":
        print("\nDesculpe, menores de idade não podem tomar vinho!")
    elif bebida in bebidas_menor:
        print(f"\nVocê escolheu {bebida}. Aproveite a festa!")
    elif bebida in ["nenhuma", "não quero", "nao quero"]:
        print("\nTudo bem, você não quis nenhuma bebida. Aproveite a festa!")
    else:
        print("\nOpção inválida. Você não escolheu uma bebida da lista.")

print("\nPrograma encerrado.")