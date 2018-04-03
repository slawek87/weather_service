# How to install

I didn't zip my virtualenv. I'm pretty sure that this solution won't work.

`pip install client/requirements.txt`
`pip install service/requirements.txt`

# Introduction

I've created 2 apps:
  * client - this application install on desktop where user updates weather.xlsx file.
  * service - this application deploy to webserver.

# Client

Client application reads data from weather.xlsx file. I've attached that file in `client/weather.xlsx`. So you can check it.

To run that application use command `python run_weather_client.py`.

I've implemented registry for reading file. It means that in each new job, script reads the last line of
`logs/reader.log`. In this file script stores all numbers of read lines. The last line defines rows to skip from xlsx file.

It will be useful when weather.xlsx file will have thousands of lines :) script reads just those lines what have never
read before.

Client application also sends post request with json data to `upload` rest api endpoint.

Job tasks were implemented by https://pypi.python.org/pypi/schedule. It's pretty easy and fast in implementation.
Firstly I was trying to setup it with Crontab but I got some problems with activate virtualenv and I didn't have enough time
to do better research and resolve that problem. So this is why I used `schedule`.

# Service

endpoints:
    `0.0.0.0:8000/api/v1/weather/stats/retrieve` [GET]
    `0.0.0.0:8000/api/v1/weather/list` [GET]
    `0.0.0.0:8000/api/v1/weather/upload` [POST]

In `upload view` I used django-q async task to queue requests.

In `WeatherStatsModel` I store all information about stats. I assumed that we can have thousands of records.
So it's better to create separate model where we can store already calculated stats.

Model stores history of information when and what kind of stats were created.

`WeatherStatsModel.last_id` stores the last `id` of record what we used to calculate last stats.
`WeatherStatsModel.sum_temperature`, `WeatherStatsModel.sum_temperature`, `{direction}_direction` those are help fields
to update stats without re-calculating everything from the beginning. It should saves some $$$ when db is bigger ^^

I decided to use django-q. It's easy to manage scheduled tasks and monitoring them.

`calculate_stats()` should be added as a schedule task in django admin:
    1. `http://0.0.0.0:8000/admin/django_q/schedule/`
    2. In field `func` add `weather.models.calculate_stats`
    3. `Schedule Type`, `Repeats`, `Next Run` setup them with your preferences.

Tasks monitoring:
    - `http://0.0.0.0:8000/admin/django_q/failure/`
    - `http://0.0.0.0:8000/admin/django_q/success/`

# other things

Guys.. are you sure that this task was for 2hrs for one programmer? :)
I spent 8hrs.. and I'm sure that I would like to spend next 18hrs on that task :) I didn't implement tests.
I didn't make good research about python CronTab. I didn't make codereview. I didn't even make good manual tests :))

I would like to check idea with live streaming data from .xlsx file.. and read something about db and statistics..
probably no-sql db would be better choice then postgresql.

p.s.
In `service/conf/site_settings.py` you will find my config.





