from django.core.mail import send_mail
from django.conf import settings
from django.template.defaultfilters import slugify as d_slugify
from django.shortcuts import render
import schedule
import time

import mailing.models


def convert_word(words) -> str:
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


def my_scheduled_job():
    print("sadasdas")
    # sendmail("n.avramenko87@yandex.ru", "TEST", "TEST")
    # sendmail("n.avramenko87@gmail.com", "TEST_TODAY", "TEST")
    # sendmail("anv@woori.ru", "TEST_TODAY", "TEST")
    active_transmissions = mailing.models.Transmission.objects.filter(is_published=True)
    for transmission in active_transmissions:
        print(transmission)
        print(transmission.time)
        print(transmission.frequency)


def run_schedule(request):
    if request.method == "GET":
        print("I'm working...")
        # schedule.every(1).minutes.do(my_scheduled_job)
        schedule.every(2).seconds.do(my_scheduled_job, name='Alice')
        while True:
            schedule.run_pending()
            time.sleep(10)
    return render(request, "mailing/run_scheduler.html")
