import os
import sys
from PyQt5.QtWidgets import QApplication

from WeatherApp.application.controller import WeatherController
from WeatherApp.presentation.emoji import WeatherEmojiResolver
from WeatherApp.presentation.widget import WeatherAppWindow

from WeatherApp.infrastructure.openweather.config import OpenWeatherConfig
from WeatherApp.infrastructure.openweather.client import OpenWeatherClient
from WeatherApp.infrastructure.openweather.mapper import OpenWeatherMapper
from WeatherApp.infrastructure.openweather.provider import OpenWeatherProvider


def build_window() -> WeatherAppWindow:
    api_key = os.getenv("OPENWEATHER_API_KEY") or "Your api key"

    config = OpenWeatherConfig(api_key=api_key)
    client = OpenWeatherClient(config)
    mapper = OpenWeatherMapper()
    provider = OpenWeatherProvider(client, mapper)

    controller = WeatherController(provider, WeatherEmojiResolver())
    return WeatherAppWindow(controller)


def main() -> None:
    qt_app = QApplication(sys.argv)
    window = build_window()
    window.show()
    sys.exit(qt_app.exec_())


if __name__ == "__main__":
    main()
