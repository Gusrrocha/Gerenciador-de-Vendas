 # classe principal
from model.peca import Peca
from model.cliente import Cliente
from model.clientedao import *

for i in range(0,15):
    novo_cliente = Cliente(i, f'Cliente - {i}', 'rua da rua', '31435245254')
    add(novo_cliente)
for p in range(0,15):
    nova_peca = Peca(p, f'Peca - {p}', 'Valor - 545', 'Validade - 23/08')
    add(nova_peca)
listAll()
