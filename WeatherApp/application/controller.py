from dataclasses import dataclass

from WeatherApp.application.interfaces import IWeatherProvider
from WeatherApp.domain.errors import BadRequestError
from WeatherApp.presentation.emoji import WeatherEmojiResolver


@dataclass(frozen=True)
class WeatherViewModel:
    """
    ViewModel:
    UI-ready data (strings and emoji).
    UI does NOT do conversions; it simply displays these fields.
    """
    temperature_text: str
    emoji: str
    description_text: str


class WeatherController:
    """
    Controller (Use Case / Application Layer):

    Responsibilities:
    - Validate user input (city)
    - Call provider to fetch weather (Domain)
    - Convert Domain -> ViewModel (UI-friendly)
    """

    def __init__(self, provider: IWeatherProvider, emoji_resolver: WeatherEmojiResolver) -> None:
        # Store dependencies for later use
        self._provider = provider
        self._emoji = emoji_resolver

    def get_weather_for_city(self, city: str) -> WeatherViewModel:
        """
        This is the main use-case method the UI calls.

        Parameters:
          city: user-entered text from QLineEdit

        Returns:
          WeatherViewModel: ready to display in the UI
        """

        # Normalize input (handle None or whitespace)
        city = (city or "").strip()

        # Validation rule: must not be empty
        if not city:
            # Raise app-specific error that UI will catch and display
            raise BadRequestError("Please enter a city name.")

        # Ask provider for Domain model (WeatherReport)
        report = self._provider.get_current(city)

        # Convert Domain -> ViewModel
        # - temperature becomes formatted string
        # - weather id becomes emoji
        # - description is passed through
        return WeatherViewModel(
            temperature_text=f"{report.temp_f:.0f}°F",
            emoji=self._emoji.from_weather_id(report.weather_id),
            description_text=report.description,
        )
