# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

import model.clientedao as funcoes_clientes
import model.pecadao as peda_dao
from model.cliente import Cliente
from model.peca import Peca


    # add peças

# cria a aplicação
app = QApplication(sys.argv)
# definir os widgets que aparecerão na tela
window = MainWindow()
window.show() # carregar o elemento para a tela
app.setStyle('Fusion')
#executar o aplicativo
app.exec()