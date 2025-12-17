from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherReport:
    city: str
    temp_f: float
    weather_id: int
    description: str
