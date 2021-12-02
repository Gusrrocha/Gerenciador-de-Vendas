
# Padrão DAO (data acess object)
# Centraliza o acesso aos dados dos objetos cliente
from model.cliente import Cliente
lista_clientes = []
#pega um cliente pelo ID
def getCliente(id):
    for c in lista_clientes:
        if c.id == id:
            return c #retornar
    
    # CASO não encontrar o cliente com o ID informado
    return None
# adicionar novo cliente
def add(novo_cliente):
    lista_clientes.append(novo_cliente)
# editar novo cliente
# Editar cliente - Dado um objeto cliente, achá-lo na lista e atualiza-lo
def edit(cliente):
    # achar a posição na lista em que o cliente editado está armazenado
    for index in range(0, len(lista_clientes)):
        cliente_atual = lista_clientes[index]
        if cliente.id == cliente_atual.id:
            # se forem iguais significa que o cliente está armazenado
            # na posição definida pelo index
            lista_clientes[index] = cliente # substitui o objeto da posição informada pelo index
            return
            
# excluir cliente
# Dado o ID do cliente, removê-lo da lista
def delete(id_cliente):
    for index in range(0, len(lista_clientes)):
        cliente_atual = lista_clientes[index]
        if id_cliente == cliente_atual.id:
            del lista_clientes[index]

            return

# listar todos os clientes
def listAll():
    for c in lista_clientes:
        c.imprime()
    
    
# pegar um cliente específico
# Dado o ID do cliente, imprimir seus dados
def listar_todos(id):
    pass