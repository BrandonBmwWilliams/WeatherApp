from WeatherApp.domain.models import WeatherReport


class OpenWeatherMapper:
    @staticmethod
    def to_report(data: dict) -> WeatherReport:
        city = data.get("name", "Unknown")
        temp_f = float(data["main"]["temp"])
        weather_id = int(data["weather"][0]["id"])
        description = str(data["weather"][0]["description"])

        return WeatherReport(
            city=city,
            temp_f=temp_f,
            weather_id=weather_id,
            description=description,
        )
