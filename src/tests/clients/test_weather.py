"""
Тестирование функций клиента для получения информации о погоде.
"""


import pytest

from clients.weather import WeatherClient
from settings import API_KEY_OPENWEATHER


class TestClientWeather:
    """
    Тестирование клиента для получения информации о странах.
    """

    base_url = "https://api.openweathermap.org/data/2.5/weather"

    @pytest.fixture
    def client(self):
        return WeatherClient()

    @pytest.mark.asyncio
    async def test_get_base_url(self, client):
        assert await client.get_base_url() == self.base_url

    @pytest.mark.asyncio
    async def test_get_countries(self, mocker, client):
        mocker.patch("clients.base.BaseClient._request")
        await client.get_weather("test")
        await client._request(
            f"{self.base_url}?units=metric&q=test&appid={API_KEY_OPENWEATHER}"
        )
