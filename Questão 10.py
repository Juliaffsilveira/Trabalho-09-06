numeros = []

# Laço para coletar 5 números inteiros
for i in range(5):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)

# Inicializa as variáveis de controle usando o primeiro número como referência
maior = numeros[0]
menor = numeros[0]

# Varredura para encontrar o maior e o menor valor
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

# Exibição dos resultados
print("\nTodos os números inseridos: ", end="")
for n in numeros:
    print(f"{n}  ", end="")  # end="" serve para não quebrar a linha a cada número

print(f"\nMaior número encontrado: {maior}")
print(f"Menor número encontrado: {menor}")