import gui
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog



class MainForm(QMainWindow):
    def __init__(self,parent=None):
        super(MainForm,self).__init__(parent)
        self.ui = gui.Ui_Form()
        self.ui.setupUi(self)
    def open(self):
        file = QFileDialog.getOpenFileName()
if __name__ == "__main__":

    app = QApplication(sys.argv)

    form = MainForm()

    form.show()
    
    exit(app.exec_())
