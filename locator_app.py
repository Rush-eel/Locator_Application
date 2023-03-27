from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTabWidget, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io


class ui_window(object):
    # Setting up main window
    def setup_window(self, window):
        window.setWindowTitle("Locator")
        window.setFixedWidth(530)
        window.setFixedHeight(600)
        self.setup_tabs()
    # Setting up area to edit, text boxes, text, and more
    def setup_tabs(self):
        self.centralWidget = QWidget(window)
        self.centralWidget.setFixedWidth(1050)
        self.centralWidget.setFixedHeight(600)
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setFixedWidth(1050)
        self.tabWidget.setFixedHeight(600)
        self.latLabel = QLabel(self.tabWidget)
        self.latLabel.setText("Latitude:")
        self.latLabel.move(30, 20)
        self.latLabel.setStyleSheet("font-size: 20pt")
        self.longLabel = QLabel(self.tabWidget)
        self.longLabel.setText("Longitude:")
        self.longLabel.move(30, 70)
        self.longLabel.setStyleSheet("font-size: 20pt")
        self.locButton = QPushButton(self.tabWidget)
        self.locButton.setText("Locate")
        self.locButton.move(410, 30)
        self.locButton.resize(100, 60)
        self.locButton.clicked.connect(self.map)
        self.lattextbox = QLineEdit(self.tabWidget)
        self.lattextbox.move(112, 19)
        self.lattextbox.resize(280, 30)
        self.lattextbox.setText("0")
        self.longtextbox = QLineEdit(self.tabWidget)
        self.longtextbox.move(128, 70)
        self.longtextbox.resize(265, 30)
        self.longtextbox.setText("0")
        self.map_container = QtWidgets.QGroupBox(self.centralWidget)
        self.map_container.setGeometry(QtCore.QRect(15, 100, 500, 500))
        self.map_container.setEnabled(True)
        self.map_container.setFlat(True)
    # Setting up map, and updating map whenever the locate button is pushed
    def map(self):
        self.map_frame = QtWidgets.QVBoxLayout(self.map_container)
        la = int(self.lattextbox.text())
        lo = int(self.longtextbox.text())
        coordinate = (la,lo)
        map = folium.Map(zoom_start=3, location=coordinate)
        folium.Marker(
                location=coordinate,
                icon=folium.Icon(color="red", icon='circle', prefix='fa'),
            ).add_to(map)
        data = io.BytesIO()
        map.save(data, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.map_frame.addWidget(webView)
        self.map_frame.deleteLater()

# System exit
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ui_window()
    ui.setup_window(window)
    window.show()
    sys.exit(app.exec_())




