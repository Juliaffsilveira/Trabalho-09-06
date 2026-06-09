media = float(input("Digite a média do aluno (0.0 a 10.0): "))
frequencia = float(input("Digite a frequência do aluno em % (0 a 100): "))

# Uso do operador lógico 'and' (equivalente ao 'e' do Portugol)
if media >= 7.0 and frequencia >= 75.0:
    print("\n----------------------------------------")
    print("Resultado: Aluno APROVADO!")
    print("----------------------------------------")
else:
    print("\n----------------------------------------")
    print("Resultado: Aluno REPROVADO.")
    print("----------------------------------------")