from typing import Optional, Dict, Any
import requests

from WeatherApp.domain.errors import (
    WeatherError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    CityNotFoundError,
    ServerError,
    NetworkError,
)
from WeatherApp.infrastructure.openweather.config import OpenWeatherConfig


class OpenWeatherClient:
    def __init__(self, config: OpenWeatherConfig, session: Optional[requests.Session] = None) -> None:
        self._config = config
        self._session = session or requests.Session()

    def fetch_current(self, city: str) -> Dict[str, Any]:
        params = {"q": city, "appid": self._config.api_key, "units": self._config.units}

        try:
            resp = self._session.get(self._config.base_url, params=params, timeout=10)
        except requests.exceptions.RequestException as ex:
            raise NetworkError("Connection error: check your internet connection.") from ex

        try:
            data = resp.json()
        except ValueError:
            data = {}

        if resp.status_code == 200:
            return data

        self._raise_for_status(resp.status_code)
        raise WeatherError("Unexpected error occurred.")

    @staticmethod
    def _raise_for_status(status_code: int) -> None:
        if status_code == 400:
            raise BadRequestError("Bad request: please check your input.")
        if status_code == 401:
            raise UnauthorizedError("Unauthorized: please check your API key.")
        if status_code == 403:
            raise ForbiddenError("Forbidden: access is denied.")
        if status_code == 404:
            raise CityNotFoundError("City not found: please check the spelling.")
        if status_code in (500, 502, 503, 504):
            raise ServerError("Weather service is having issues. Try again later.")
        raise WeatherError(f"HTTP error occurred (status {status_code}).")
