class WeatherError(Exception):
    """
    Base app-specific exception.
    The UI catches WeatherError so it can show a user-friendly message
    without crashing the app.
    """
    pass


# Specific error types let you handle different failure scenarios cleanly.
class BadRequestError(WeatherError):
    """Example: user entered empty city, or request was malformed."""
    pass


class UnauthorizedError(WeatherError):
    """Example: API key missing/invalid (401)."""
    pass


class ForbiddenError(WeatherError):
    """Example: access denied (403)."""
    pass


class CityNotFoundError(WeatherError):
    """Example: city not found (404)."""
    pass


class ServerError(WeatherError):
    """Example: OpenWeather server having problems (5xx)."""
    pass


class NetworkError(WeatherError):
    """Example: no internet / DNS / timeout / requests exceptions."""
    pass
