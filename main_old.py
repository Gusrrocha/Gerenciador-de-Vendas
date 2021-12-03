 # classe principal
from model.peca import Peca
from model.cliente import Cliente
from model.clientedao import *

# ADICIONAR CLIENTES
for i in range(0,15):
    novo_cliente = Cliente(i, f'Cliente - {i}', 'rua da rua', '31435245254')
    # CHAMADA DA FUNÇÃO DE ADICIONAR UM CLIENTE EM CLIENTE DAO.PY
    add(novo_cliente)
# EXCLUIR UM CLIENTE
delete(13)
delete(12)

# EDIÇÃO DE UM CLIENTE

# 1 - Qual o ID do cliente que deseja entrar
# id_cliente = 4

# 2 - Pegar todas as informações do cliente
get_cliente = getCliente(3)

# 3 - Fazer a edição dos campos localmente
get_cliente.nome = 'Gustavo Rocha'
get_cliente.endereco = 'Rua da rua'
get_cliente.telefone = '71 9 314134143'

# 4 - salvar o elemento na lista
edit(get_cliente)

# 5 - Lista todos os clientes
listAll()

# 6 - 