import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Web Engine
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)

        # Menu/Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction(u'\u2190', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction(u'\u2192', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(u'\u27f3', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.home_site)
        navbar.addAction(home_btn)

        # Search-box in Menu
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.url_site)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        self.showMaximized()

    def home_site(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def url_site(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):
        self.url_bar.setText(url.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Chrome')
window = MainWindow()
app.exec()
