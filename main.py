import sys
import os
import configparser
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class HelpSystemApp(QMainWindow):
    def __init__(self):
        super().__init__()
      
        self.config = configparser.ConfigParser()

        # Cambiar para buscar config.ini correctamente cuando se ejecuta como un ejecutable
        if getattr(sys, 'frozen', False):
            # Si está ejecutándose desde el ejecutable
            bundle_dir = sys._MEIPASS
            config_path = os.path.join(bundle_dir, 'config.ini')
        else:
            # Si está ejecutándose desde el entorno de desarrollo
            config_path = 'config.ini'

        self.config.read(config_path)

        self.setWindowTitle('Sistema de Ayuda')
        self.setGeometry(100, 100, 1200, 800)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        
        nav_layout = QHBoxLayout()

        
        home_button = QPushButton('🏠', self)
        home_button.clicked.connect(self.go_home)
        nav_layout.addWidget(home_button)

        
        back_button = QPushButton('⬅', self)
        back_button.clicked.connect(self.go_back)
        nav_layout.addWidget(back_button)

        self.has_gone_back = False
        if self.config.getboolean('AppSettings', 'forward_button_enabled', fallback=False):
            self.forward_button = QPushButton('➡', self)
            self.forward_button.setEnabled(False)  
            self.forward_button.clicked.connect(self.go_forward)
            nav_layout.addWidget(self.forward_button)

    
        search_layout = QHBoxLayout()
        if self.config.getboolean('AppSettings', 'search_icon_enabled', fallback=False):

            search_icon = QPushButton('🔍', self)
            search_icon.clicked.connect(self.search_page)  
            search_layout.addWidget(search_icon)
        
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Buscar...")
        self.search_bar.returnPressed.connect(self.search_page) 
        search_layout.addWidget(self.search_bar)

        nav_layout.addLayout(search_layout)
        main_layout.addLayout(nav_layout)

        self.browser = QWebEngineView()
        main_layout.addWidget(self.browser)

       
        self.base_path = os.path.abspath(os.path.dirname(__file__))
        self.html_folder = os.path.join(self.base_path, 'html_files')  
        self.load_html_page('introduccion.html')  

    def load_html_page(self, page):
        page_path = os.path.join(self.html_folder, page)
        page_url = QUrl.fromLocalFile(page_path)

        if os.path.exists(page_path):
            self.browser.setUrl(page_url)
        else:
            print(f"Error: {page} no encontrado en {self.html_folder}")

    def go_home(self):
        self.load_html_page('introduccion.html')

    def go_back(self):
        self.browser.back()
        self.has_gone_back = True
        if hasattr(self, 'forward_button'):
            self.forward_button.setEnabled(True)

    def go_forward(self):
        self.browser.forward()

    def search_page(self):
        query = self.search_bar.text().replace(" ", "_")
        if query:
            search_page = f"{query}.html"
            self.load_html_page(search_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpSystemApp()
    window.show()

    sys.exit(app.exec_())
