from typing import Protocol
from WeatherApp.domain.models import WeatherReport


class IWeatherProvider(Protocol):
    """
    Protocol = interface-like contract in Python.

    Anything that implements this method signature can be used as a provider.
    This is DIP (Dependency Inversion):
    - Controller depends on this abstraction, not a concrete OpenWeather provider.
    """

    def get_current(self, city: str) -> WeatherReport:
        """
        Input: city name string (e.g., "Phoenix")
        Output: domain WeatherReport object
        """
        ...
