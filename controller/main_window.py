# Classe que irá controlar o main_window.ui

from qt_core import *
FILE_UI = 'view/mainwindow.ui'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)