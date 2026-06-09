# Coleta de dados (input sempre lê como texto/string)
nome = input("Digite o seu nome: ")

# int() converte o texto para número inteiro
idade = int(input("Digite a sua idade: "))

# float() converte o texto para número real/decimal
altura = float(input("Digite a sua altura (ex: 1.75): "))

# Exibição formatada usando f-strings
print("\n----------------------------------------")
print("Cadastro realizado com sucesso:")
print("----------------------------------------")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f}m")
print("----------------------------------------")