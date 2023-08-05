from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, \
    QLineEdit, QPushButton, QMenuBar, QMenu, QLabel, QGridLayout, QVBoxLayout, QTextEdit, \
        QTableWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
class GUI(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()

        self.setWindowTitle('sukupuuohjelma')       
        self.setGeometry(0, 28, 1000, 750)        
        
#        self._createMenuBar()
               
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.m_w11 = QWidget()
        self.m_w12 = QWidget()
        self.m_w21 = QWidget()
        self.m_w22 = QWidget()

        layout = QGridLayout(central_widget)

        for w, (r, c) in zip(
            (self.m_w11, self.m_w12, self.m_w21, self.m_w22),
            ((0, 0), (0, 1), (1, 0), (1, 1)),
        ):
            layout.addWidget(w, r, c)
        for c in range(2):
            layout.setColumnStretch(c, 1)
        for r in range(2):
            layout.setRowStretch(r, 1)

        layout = QVBoxLayout(self.m_w11)
        layout.addWidget(QTableWidget())

        layout = QVBoxLayout(self.m_w12)
        layout.addWidget(self.webView)

        layout = QVBoxLayout(self.m_w21)
        layout.addWidget(QLineEdit())

        layout = QVBoxLayout(self.m_w22)
        layout.addWidget(QLabel("Text", alignment=Qt.AlignmentFlag.AlignCenter))
        
#    def _createMenuBar(self):
#        menuBar = QMenuBar(self)
#        fileMenu = QMenu("&File", self)
#        menuBar.addMenu(fileMenu)