import os
import sys
from PyQt5.QtWidgets import QApplication

# Controller = "use-case" logic (validates input, orchestrates provider, returns UI-friendly data)
from WeatherApp.application.controller import WeatherController

# Small helper that maps weather ids to emojis
from WeatherApp.presentation.emoji import WeatherEmojiResolver

# The PyQt UI window (presentation layer)
from WeatherApp.presentation.widget import WeatherAppWindow

# Infrastructure pieces for OpenWeather
from WeatherApp.infrastructure.openweather.config import OpenWeatherConfig
from WeatherApp.infrastructure.openweather.client import OpenWeatherClient
from WeatherApp.infrastructure.openweather.mapper import OpenWeatherMapper
from WeatherApp.infrastructure.openweather.provider import OpenWeatherProvider


def build_window() -> WeatherAppWindow:
    """
    Composition Root / Wiring Function:
    - Creates ALL objects and injects dependencies.
    - Returns a fully configured UI window.
    """

    # Get API key from environment variable if available; fallback to placeholder if not
    api_key = os.getenv("OPENWEATHER_API_KEY") or "YOUR_API_KEY_HERE"

    # Bundle API settings into a config object (data only)
    config = OpenWeatherConfig(api_key=api_key)

    # Create a networking client (responsible only for HTTP calls & translating status codes)
    client = OpenWeatherClient(config)

    # Create mapper (responsible only for converting JSON -> domain WeatherReport)
    mapper = OpenWeatherMapper()

    # Create provider (implements IWeatherProvider) using client + mapper
    provider = OpenWeatherProvider(client, mapper)

    # Create controller (orchestrates and converts Domain -> ViewModel)
    controller = WeatherController(provider, WeatherEmojiResolver())

    # Create and return the UI window with controller injected
    return WeatherAppWindow(controller)


def main() -> None:
    """
    Program entry point:
    - Starts Qt application loop
    - Builds window and shows it
    """

    # QApplication manages the Qt event loop and application-level resources
    qt_app = QApplication(sys.argv)

    # Build the app's main window with all dependencies wired
    window = build_window()

    # Show window on screen
    window.show()

    # Start Qt event loop; exit Python process when the UI closes
    sys.exit(qt_app.exec_())


# Standard Python entry-point check (prevents running main() when imported as a module)
if __name__ == "__main__":
    main()
