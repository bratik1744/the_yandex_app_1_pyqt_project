from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import classes_UI
from PyQt5.QtCore import QFile, QTextStream

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile("darkstyle.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    ex = classes_UI.Menu()
    ex.show()
    sys.exit(app.exec_())
