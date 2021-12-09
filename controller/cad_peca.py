from qt_core import *
from model.peca import Peca
import model.pecadao as funcoes_pecas
FILE_UI = 'view/cad_peca.ui'
class CadPecaWindow(QWidget):
    def __init__(self, janela_cliente):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.janela_cliente = janela_cliente


        # evento dos botões
        self.cancelar_btn.clicked.connect(self.fechar_janela)
        self.salvar_btn.clicked.connect(self.salvar)

    def fechar_janela(self):
        self.close() #close - fechar

    def salvar(self):
        # pega os dados dos clientes
        nome = self.nome.text()
        validade = self.validade.value()
        valor = self.valor.text()

        nova_peca = Peca(None, nome, valor, validade)
        funcoes_pecas.add(nova_peca)

        self.janela_cliente.carrega_dados()

        self.close()
