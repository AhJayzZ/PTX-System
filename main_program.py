
from PyQt5.QtWidgets import QApplication
from UI.homePage import HomePage
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    initialPage = HomePage()
    sys.exit(app.exec_())