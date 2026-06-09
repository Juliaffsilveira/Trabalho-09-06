nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Cálculo da média aritmética
media = (nota1 + nota2) / 2

# Verificação das faixas de notas
if media >= 7.0:
    print(f"\nMédia: {media:.1f} - Status: APROVADO!")
elif media >= 5.0:
    print(f"\nMédia: {media:.1f} - Status: RECUPERAÇÃO.")
else:
    print(f"\nMédia: {media:.1f} - Status: REPROVADO.")