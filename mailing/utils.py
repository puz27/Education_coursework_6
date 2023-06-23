from django.core.mail import send_mail
from django.conf import settings
from django.template.defaultfilters import slugify as d_slugify
from django.views.debug import ExceptionReporter
from django_cron import CronJobBase, Schedule


def slugify(words: str) -> str:
    """
    Slugify for russian language.
    """
    alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z',
                'и': 'i',
                'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e',
                'ю': 'yu',
                'я': 'ya'}

    return d_slugify(''.join(alphabet.get(w, w) for w in words.lower()))


def sendmail(to, subject, message):
    send_mail(subject,
              message,
              settings.EMAIL_HOST_USER,
              [to],
              fail_silently=True
            )


class MyCronJob(CronJobBase):
    RUN_EVERY_MINUTES = 1
    RUN_AT_TIMES = ['11:30', '14:00', '23:15']
    schedule = Schedule(run_at_times=RUN_EVERY_MINUTES)

    def do_work(self):
        sendmail("anv@woori.ru", "TEST", "TEST")

MyCronJob.RUN_AT_TIMES.append(13)