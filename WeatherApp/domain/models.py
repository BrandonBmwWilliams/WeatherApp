from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherReport:
    """
    Domain Model:
    This is the internal representation of weather data *for your app*.
    It avoids passing raw JSON around and makes the rest of the app stable.

    frozen=True makes it immutable:
    - Once created, fields cannot change
    - Helps reduce bugs and makes it safe to share
    """
    city: str
    temp_f: float
    weather_id: int
    description: str
