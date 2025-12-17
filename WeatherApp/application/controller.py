from dataclasses import dataclass

from WeatherApp.application.interfaces import IWeatherProvider
from WeatherApp.domain.errors import BadRequestError
from WeatherApp.presentation.emoji import WeatherEmojiResolver


@dataclass(frozen=True)
class WeatherViewModel:
    temperature_text: str
    emoji: str
    description_text: str


class WeatherController:
    def __init__(self, provider: IWeatherProvider, emoji_resolver: WeatherEmojiResolver) -> None:
        self._provider = provider
        self._emoji = emoji_resolver

    def get_weather_for_city(self, city: str) -> WeatherViewModel:
        city = (city or "").strip()
        if not city:
            raise BadRequestError("Please enter a city name.")

        report = self._provider.get_current(city)

        return WeatherViewModel(
            temperature_text=f"{report.temp_f:.0f}°F",
            emoji=self._emoji.from_weather_id(report.weather_id),
            description_text=report.description,
        )
