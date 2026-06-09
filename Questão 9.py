# Criação de um dicionário nativo usando a estrutura chave: valor
aluno = {
    "nome": input("Digite o nome do aluno: "),
    "idade": int(input("Digite a idade do aluno: ")),
    "curso": input("Digite o curso do aluno: ")
}

print("\n--- Dados Estruturados (Dicionário) ---")
# O método .items() permite acessar a chave e o valor ao mesmo tempo no laço
for chave, valor in aluno.items():
    print(f"CHAVE: '{chave}' -> VALOR: {valor}")