# Entrada e conversão dos dados para número real (float)
valor = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Processamento aritmético básico
soma = valor + valor2
subtracao = valor - valor2
multiplicacao = valor * valor2

print(f"\nO resultado da soma é: {soma}")
print(f"O resultado da subtração é: {subtracao}")
print(f"O resultado da multiplicação é: {multiplicacao}")

# Cláusula de segurança para evitar erro de divisão por zero
if valor2 != 0:
    divisao = valor / valor2
    print(f"O resultado da divisão é: {divisao}")
else:
    print("O resultado da divisão é: Erro (Não é possível dividir por zero)")