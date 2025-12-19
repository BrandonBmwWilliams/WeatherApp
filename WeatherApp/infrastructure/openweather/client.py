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
    """
    HTTP client for OpenWeather.

    Responsibilities:
    - Build request params
    - Make HTTP call using requests
    - Convert network + HTTP status problems into WeatherError types
    """

    def __init__(self, config: OpenWeatherConfig, session: Optional[requests.Session] = None) -> None:
        # Store config so we know API key, URL, units
        self._config = config

        # Use passed-in session if given (helps testing), otherwise create one
        self._session = session or requests.Session()

    def fetch_current(self, city: str) -> Dict[str, Any]:
        """
        Fetch raw JSON dict from OpenWeather for current conditions.

        Input:
          city: string

        Output:
          dict (raw JSON parsed into Python dict)
        """

        # Query parameters used by OpenWeather API
        params = {"q": city, "appid": self._config.api_key, "units": self._config.units}

        try:
            # Perform GET request with a timeout so UI doesn't hang forever
            resp = self._session.get(self._config.base_url, params=params, timeout=10)

        except requests.exceptions.RequestException as ex:
            # Any request-related issue becomes a friendly NetworkError
            raise NetworkError("Connection error: check your internet connection.") from ex

        # OpenWeather typically returns JSON even on errors, but we guard just in case
        try:
            data = resp.json()
        except ValueError:
            data = {}

        # Success: return the JSON dict
        if resp.status_code == 200:
            return data

        # Otherwise translate status code into specific WeatherError
        self._raise_for_status(resp.status_code)

        # Fallback (shouldn't usually happen because _raise_for_status raises)
        raise WeatherError("Unexpected error occurred.")

    @staticmethod
    def _raise_for_status(status_code: int) -> None:
        """
        Convert HTTP status codes into domain/app-friendly exceptions.
        """
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

        # Unknown status code
        raise WeatherError(f"HTTP error occurred (status {status_code}).")
