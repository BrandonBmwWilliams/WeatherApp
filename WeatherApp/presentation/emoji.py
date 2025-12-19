class WeatherEmojiResolver:
    """
    Presentation helper:
    Maps OpenWeather condition IDs to emojis.

    Keeping this separate:
    - UI doesn't need to know the rules
    - Controller/UI can reuse it
    - Easy to change later
    """

    @staticmethod
    def from_weather_id(weather_id: int) -> str:
        """
        Input: weather condition id from OpenWeather (e.g., 800)
        Output: emoji string
        """
        if 200 <= weather_id <= 232:
            return "⛈️"
        if 300 <= weather_id <= 321:
            return "🌦️"
        if 500 <= weather_id <= 531:
            return "🌧️"
        if 600 <= weather_id <= 622:
            return "❄️"
        if 701 <= weather_id <= 741:
            return "🌫️"
        if weather_id == 762:
            return "🌋"
        if weather_id == 771:
            return "💨"
        if weather_id == 781:
            return "🌪️"
        if weather_id == 800:
            return "☀️"
        if 801 <= weather_id <= 804:
            return "☁️"

        # fallback if we don't recognize the id
        return "❔"
