class Cliente:
    clientes = []

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Cliente.clientes.append(self)

    @classmethod
    def buscar_cliente(cls, nome):
        for cliente in cls.clientes:
            if cliente.nome == nome:
                return cliente
        return None

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(f"Nome: {cliente.nome}, Idade: {cliente.idade}")

# Instanciando objetos da classe Cliente
cliente1 = Cliente("Ana", 25)
cliente2 = Cliente("João", 30)
cliente3 = Cliente("Maria", 28)

# Acessando a lista de clientes
print("Lista de Clientes:")
Cliente.listar_clientes()

# Buscando um cliente pelo nome
nome_busca = "João"
cliente_encontrado = Cliente.buscar_cliente(nome_busca)
if cliente_encontrado:
    print(f"Cliente {nome_busca} encontrado: Idade {cliente_encontrado.idade}")
else:
    print(f"Cliente {nome_busca} não encontrado.")
