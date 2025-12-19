from WeatherApp.domain.models import WeatherReport


class OpenWeatherMapper:
    """
    Mapper:
    Transforms OpenWeather JSON dict into a WeatherReport (domain model).
    """

    @staticmethod
    def to_report(data: dict) -> WeatherReport:
        """
        Input: raw OpenWeather JSON dict
        Output: WeatherReport domain object
        """

        # Extract from OpenWeather's JSON structure
        city = data.get("name", "Unknown")
        temp_f = float(data["main"]["temp"])
        weather_id = int(data["weather"][0]["id"])
        description = str(data["weather"][0]["description"])

        # Build domain model instance
        return WeatherReport(
            city=city,
            temp_f=temp_f,
            weather_id=weather_id,
            description=description,
        )
