from client.libs.registry import register_job
from client.libs.weather import upload


def init_job(weather_xls):
    """Initialize job."""
    register_job(comment="Run weather task")
    upload(weather_xls)


def setup(weather_xls):
    """Function setup schedule."""
    init_job(weather_xls)
    # schedule.every(1).minutes.do(init_job, weather_xls)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
