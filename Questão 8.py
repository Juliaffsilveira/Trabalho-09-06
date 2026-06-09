# Inicializa uma lista dinâmica vazia
lista_compras = []

print("--- Preenchendo a Lista de Compras ---")
# Laço para repetir a entrada de dados 5 vezes
for i in range(5):
    item = input(f"Digite o {i + 1}º item: ")
    lista_compras.append(item)  # Adiciona o item digitado ao final da lista

print("\n--- Itens na sua Lista ---")
# Varredura direta da lista para exibição
for item in lista_compras:
    print(f"- {item}")