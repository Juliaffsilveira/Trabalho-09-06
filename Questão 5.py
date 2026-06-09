numero = float(input("Digite um número qualquer: "))

# Estrutura condicional utilizando if, elif (senao se) e else (senao)
if numero > 0:
    print(f"\nO número {numero} é POSITIVO.")
elif numero < 0:
    print(f"\nO número {numero} é NEGATIVO.")
else:
    print("\nO número digitado é ZERO.")