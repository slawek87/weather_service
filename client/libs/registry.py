import datetime
from os import path

# default settings
dir_path = path.dirname(path.abspath(__file__))
default_job_registry = path.join(dir_path, '..', 'logs', 'job_registry.log')
default_reader_registry = path.join(dir_path, '..', 'logs', 'reader.log')


def register_job(comment, job_registry=None):
    """
    Function logs information about run cron jobs.
    """
    with open(job_registry or default_job_registry, 'a') as entry_log:
        content = '{comment} {datetime}\n'.format(comment=comment, datetime=datetime.datetime.now())
        entry_log.write(content)


def register_reader(last_row_number, reader_registry=None):
    """
    Function logs information about number of the last read row.
    """
    with open(reader_registry or default_reader_registry, 'a') as entry_log:
        content = '{last_row_number}\n'.format(last_row_number=last_row_number)
        entry_log.write(content)
