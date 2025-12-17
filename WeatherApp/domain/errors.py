class WeatherError(Exception):
    """Base exception type for predictable, user-facing weather errors."""
    pass


class BadRequestError(WeatherError):
    pass


class UnauthorizedError(WeatherError):
    pass


class ForbiddenError(WeatherError):
    pass


class CityNotFoundError(WeatherError):
    pass


class ServerError(WeatherError):
    pass


class NetworkError(WeatherError):
    pass
