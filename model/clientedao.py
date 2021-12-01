
# Padrão DAO (data acess object)
# Centraliza o acesso aos dados dos objetos clientes

lista_clientes = []
# adicionar novo cliente
def add(novo_cliente):
    lista_clientes.append(novo_cliente)
# editar novo cliente
def edit():
    pass
# excluir cliente
def delete():
    pass
# listar todos os clientes
def listAll():
    for c in lista_clientes:
        c.print()
# pegar um cliente específico
def lista_cliente():
    pass