from typing import Protocol
from WeatherApp.domain.models import WeatherReport


class IWeatherProvider(Protocol):
    def get_current(self, city: str) -> WeatherReport:
        ...
