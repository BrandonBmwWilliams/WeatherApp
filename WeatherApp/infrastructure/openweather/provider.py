from WeatherApp.application.interfaces import IWeatherProvider
from WeatherApp.domain.models import WeatherReport
from WeatherApp.infrastructure.openweather.client import OpenWeatherClient
from WeatherApp.infrastructure.openweather.mapper import OpenWeatherMapper


class OpenWeatherProvider(IWeatherProvider):
    def __init__(self, client: OpenWeatherClient, mapper: OpenWeatherMapper) -> None:
        self._client = client
        self._mapper = mapper

    def get_current(self, city: str) -> WeatherReport:
        data = self._client.fetch_current(city)
        return self._mapper.to_report(data)
