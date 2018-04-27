import gui
import sys
import match
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog



class MainForm(QMainWindow):
    def __init__(self,parent=None):
        super(MainForm,self).__init__(parent)
        self.ui = gui.Ui_Form()
        self.ui.setupUi(self)
    def open(self):
        file = QFileDialog.getOpenFileName()
    def apply(self):
        cl1 = [self.ui.lineEdit.text(),self.ui.lineEdit_2.text()]
        cl2 = [self.ui.lineEdit_3.text(),self.ui.lineEdit_4.text()]
    def write(self):
        match.main()

def get(form):
    cl1 = [form.ui.lineEdit.text(),form.ui.lineEdit_2.text()]
    print(cl1)
if __name__ == "__main__":
    match.main()
    app = QApplication(sys.argv)

    form = MainForm()

    form.show()

    exit(app.exec_())
