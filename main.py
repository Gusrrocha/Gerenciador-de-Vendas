# importar as libs do PyQt
from qt_core import *
# importa a classe MainWindow - Janela Principal
from controller.main_window import MainWindow
def click():
    print("Olá, o botão foi pressionado")
# cria a aplicação
app = QApplication(sys.argv)

# definir os widgets que aparecerão na tela
window = MainWindow()
window.show() # carregar os elementos para a tela

# executar o aplicativo
app.exec()