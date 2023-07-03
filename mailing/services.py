from crontab import CronTab
from django.core.mail import send_mail
from django.conf import settings


def sendmail(to, subject, message):
    send_mail(subject,
              message,
              settings.EMAIL_HOST_USER,
              [to],
              fail_silently=True
            )


def set_cron():
    with CronTab(user=True) as cron:
        job = cron.new(command='echo hello_world')
        job.minute.every(1)
    print('cron.write() was just executed')

