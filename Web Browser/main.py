from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.setWindowTitle("NeuralNine Web Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://google.com"))

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.go_btn = QPushButton("Go")
        self.go_btn.clicked.connect(self.navigate_to_url)

        self.back_btn = QPushButton("<")
        self.back_btn.clicked.connect(self.browser.back)

        self.forward_btn = QPushButton(">")
        self.forward_btn.clicked.connect(self.browser.forward)

        nav_bar = QHBoxLayout()
        nav_bar.addWidget(self.url_bar)
        nav_bar.addWidget(self.go_btn)
        nav_bar.addWidget(self.back_btn)
        nav_bar.addWidget(self.forward_btn)

        layout = QVBoxLayout()
        layout.addLayout(nav_bar)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
window.show()
app.exec_()
