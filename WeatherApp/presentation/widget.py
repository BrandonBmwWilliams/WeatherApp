from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

from WeatherApp.application.controller import WeatherController, WeatherViewModel
from WeatherApp.domain.errors import WeatherError


class WeatherAppWindow(QWidget):
    def __init__(self, controller: WeatherController):
        super().__init__()
        self._controller = controller

        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)

        self._init_ui()

    def _init_ui(self) -> None:
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        for w in (self.city_label, self.city_input, self.temperature_label, self.emoji_label, self.description_label):
            w.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{ font-family: calibri; }
            QLabel#city_label{ font-size: 40px; font-style: italic; }
            QLineEdit#city_input{ font-size: 40px; }
            QPushButton#get_weather_button{ font-size: 30px; font-weight: bold; }
            QLabel#temperature_label{ font-size: 75px }
            QLabel#emoji_label{ font-size: 100px; font-family: Segoe UI emoji; }
            QLabel#description_label{ font-size: 50px }
        """)

        self.get_weather_button.clicked.connect(self._on_get_weather_clicked)

    def _on_get_weather_clicked(self) -> None:
        try:
            vm = self._controller.get_weather_for_city(self.city_input.text())
            self._display_weather(vm)
        except WeatherError as ex:
            self._display_error(str(ex))

    def _display_error(self, message: str) -> None:
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def _display_weather(self, vm: WeatherViewModel) -> None:
        self.temperature_label.setStyleSheet("font-size: 75px;")
        self.temperature_label.setText(vm.temperature_text)
        self.emoji_label.setText(vm.emoji)
        self.description_label.setText(vm.description_text)
