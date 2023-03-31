# Necessary modules for this project. This project uses PyQt5, folium, and io.
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTabWidget, QLabel, QWidget, QPushButton, QLineEdit, QCheckBox
from PyQt5.QtWebEngineWidgets import QWebEngineView
import folium
import io
import requests


class ui_window(object):
# The setup_window() function sets up the dimensions
# of the main window.
    def setup_window(self, window):
        window.setWindowTitle("Locator")
        window.setFixedWidth(530)
        window.setFixedHeight(600)
        self.get_location()
        print(la)
        print(lo)
        self.setup_main_layout()

    def get_ip(self):
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]
    def get_location(self):
        ip_address = self.get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        global la
        la = response.get("latitude")
        global lo
        lo = response.get("longitude")
        location_data = {
            "latitude": response.get("latitude"),
            "longitude": response.get("longitude")
        }
        return location_data
# The setup_tabs() function is used to set up the central
# widget, all the QLabels, which act as text or the text
# box. This function also creates the button, which is
# connected to the map() function.
    def setup_main_layout(self):

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
        self.locButton.move(410, 15)
        self.locButton.resize(100, 60)
        self.locButton.clicked.connect(self.map)
        self.lattextbox = QLineEdit(self.tabWidget)
        self.lattextbox.move(112, 19)
        self.lattextbox.resize(280, 30)
        self.lattextbox.setText("0.0")
        self.longtextbox = QLineEdit(self.tabWidget)
        self.longtextbox.move(128, 70)
        self.longtextbox.resize(265, 30)
        self.longtextbox.setText("0.0")
        self.auto_locate_box = QCheckBox(self.tabWidget)
        self.auto_locate_box.setText("Auto Locate")
        self.auto_locate_box.move(410, 70)
        self.auto_locate_box.resize(320, 40)
        self.auto_locate_box.stateChanged.connect(self.map)
        self.map_container = QtWidgets.QGroupBox(self.centralWidget)
        self.map_container.setGeometry(QtCore.QRect(15, 100, 500, 500))
        self.map_container.setEnabled(True)
        self.map_container.setFlat(True)
# The map() function sets up the map, making it
# ready to plot the latitude and longitude. This
# function is connected to the button, which deletes,
# and updates the map to the right coordinates.
    def map(self, state):
        global lo, la
        self.map_frame = QtWidgets.QVBoxLayout(self.map_container)
        if state != QtCore.Qt.Checked:
            la = float(self.lattextbox.text())
            lo = float(self.longtextbox.text())
        coordinate = (la,lo)
        map = folium.Map(zoom_start=10, location=coordinate)
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


# This is the part of the code that exits the
# application.
if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = ui_window()
    ui.setup_window(window)
    window.show()
    sys.exit(app.exec_())




