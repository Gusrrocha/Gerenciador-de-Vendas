from qt_core import *
from controller.cad_cliente import CadClienteWindow

FILE_UI = 'view/cliente_page.ui'

class ClientesPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        
        self.cliente_window = None
    
        # evento do botão nova peça
        self.novo_cliente_btn.clicked.connect(self.novo_cliente)

    def novo_cliente(self):
        # criação da janela de cadastro
        self.cliente_window = CadClienteWindow()
        self.cliente_window.show()