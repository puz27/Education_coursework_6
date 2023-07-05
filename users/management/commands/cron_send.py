from crontab import CronTab
from django_crontab.crontab import Crontab


def set_cron():
    with CronTab(user=True) as cron:
        job = cron.new(command='echo hello_world')
        job.minute.every(1)
    print('cron.write() was just executed')

