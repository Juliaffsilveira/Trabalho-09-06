numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")

# range(1, 11) gera os números de 1 até 10 (o limite superior 11 é exclusivo)
for contador in range(1, 11):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")