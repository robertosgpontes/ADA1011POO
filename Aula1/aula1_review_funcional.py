def adicionar_produto(estoque, produto, quantidade):
    estoque[produto] = estoque.get(produto, 0) + quantidade
    return estoque

def remover_produto(estoque, produto):
    if produto in estoque:
        del estoque[produto]
        return True
    else:
        return False

def atualizar_estoque(estoque, produto, quantidade):
    if produto in estoque:
        estoque[produto] += quantidade
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

def visualizar_estoque(estoque):
    print("Estoque:")
    for produto, quantidade in estoque.items():
        print(f"{produto}: {quantidade} unidades")

# Programa principal
estoque = {}

while True:
    print("\nOpções:")
    print("1 - Adicionar Produto")
    print("2 - Remover Produto")
    print("3 - Atualizar Estoque")
    print("4 - Visualizar Estoque")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        produto = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        estoque = adicionar_produto(estoque, produto, quantidade)
        print(f"{quantidade} unidades do produto '{produto}' adicionadas ao estoque.")

    elif opcao == 2:
        produto = input("Digite o nome do produto a ser removido: ")
        if remover_produto(estoque, produto):
            print(f"Produto '{produto}' removido do estoque.")
        else:
            print(f"Produto '{produto}' não encontrado no estoque.")

    elif opcao == 3:
        produto = input("Digite o nome do produto a ser atualizado: ")
        quantidade = int(input("Digite a quantidade a ser adicionada (negativa para remover): "))
        atualizar_estoque(estoque, produto, quantidade)

    elif opcao == 4:
        visualizar_estoque(estoque)

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Digite novamente.")
