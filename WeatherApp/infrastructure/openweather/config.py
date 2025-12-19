from dataclasses import dataclass


@dataclass(frozen=True)
class OpenWeatherConfig:
    """
    Configuration object for OpenWeather.

    Keeping config in a single object:
    - reduces repeated constants
    - makes it easy to change API base URL or units later
    """
    api_key: str
    base_url: str = "https://api.openweathermap.org/data/2.5/weather"
    units: str = "imperial"  # Fahrenheit
