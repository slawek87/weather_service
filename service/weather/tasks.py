from django_q.tasks import async, result


def task_calculate_stats():
    task_id = async('weather.models.calculate_stats', group="stats")
    result(task_id)
