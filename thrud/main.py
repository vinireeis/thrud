class Thrud:

    __weather_forecast_controller = WeatherForecastController

    @classmethod
    async def get_six_days_forecast(cls) -> ThrudResponse:
        return ''