from dataclasses import dataclass


@dataclass(frozen=True)
class OpenWeatherConfig:
    api_key: str
    base_url: str = "https://api.openweathermap.org/data/2.5/weather"
    units: str = "imperial"  # Fahrenheit
