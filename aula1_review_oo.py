class Estoque: # Inicio da Classe
    def __init__(self): #Método Construtor
        self.estoque = {} # Atributo [PUBLICO]

    def adicionar_produto(self, produto, quantidade): #Método [PUBLICO]
        self.estoque[produto] = self.estoque.get(produto, 0) + quantidade

    def remover_produto(self, produto):
        if produto in self.estoque:
            del self.estoque[produto]
            return True
        else:
            return False

    def atualizar_estoque(self, produto, quantidade):
        if produto in self.estoque:
            self.estoque[produto] += quantidade
        else:
            print(f"Produto '{produto}' não encontrado no estoque.")

    def visualizar_estoque(self):
        print("Estoque:")
        for produto, quantidade in self.estoque.items():
            print(f"{produto}: {quantidade} unidades")

# Programa principal
estoque = Estoque() # Instanciando Objeto / Construindo o Objeto / Inicializando o Objeto

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
        estoque.adicionar_produto(produto, quantidade)
        print(f"{quantidade} unidades do produto '{produto}' adicionadas ao estoque.")

    elif opcao == 2:
        produto = input("Digite o nome do produto a ser removido: ")
        if estoque.remover_produto(produto):
            print(f"Produto '{produto}' removido do estoque.")
        else:
            print(f"Produto '{produto}' não encontrado no estoque.")

    elif opcao == 3:
        produto = input("Digite o nome do produto a ser atualizado: ")
        quantidade = int(input("Digite a quantidade a ser adicionada (negativa para remover): "))
        estoque.atualizar_estoque(produto, quantidade)

    elif opcao == 4:
        estoque.visualizar_estoque()

    elif opcao == 0:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Digite novamente.")
