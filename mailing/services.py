from django.core.mail import send_mail
from django.conf import settings
from django.template.defaultfilters import slugify as d_slugify
from django.shortcuts import render
import schedule
import time
# import datetime
import mailing.models
import pytz
from datetime import datetime


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


def sendmail_after(transmission_id, emails_base, message_theme, message_body):
    for mail in emails_base:
        print("SENDING TO:", mail)
        sendmail(mail, message_theme, message_body)

    wu = mailing.models.Statistic.objects.get(transmission_id=transmission_id)
    wu.status = "FINISHED"
    wu.mail_answer = "OK"
    wu.time = datetime.now(pytz.timezone('Europe/Moscow'))
    wu.save()


def run_schedule(request):
    if request.method == "GET":
        schedule.clear()

        active_transmissions = mailing.models.Transmission.objects.filter(is_published=True)
        print("PREPARE SEND")
        # DAILY
        for transmission in active_transmissions:
            emails_base = []
            print("TRANSMISSION TITLE:", transmission.title)

            if transmission.frequency == "DAILY":
                print("TYPE: SEND DAILY")
                print("ID:", transmission.pk)
                convert_time = str(transmission.time)[:5]
                print("TIME:", convert_time)
                message = transmission.get_messages()
                print("MESSAGE THEME:", message.theme)
                print("MESSAGE BODY:", message.body)
                for client_mail in transmission.get_clients():
                    print("EMAIL:", client_mail.email)
                    emails_base.append(client_mail.email)
                    print(emails_base)

                    schedule.every().day.at(convert_time).do(sendmail_after,
                                                             emails_base=emails_base,
                                                             message_theme=message.theme,
                                                             message_body=message.body,
                                                             transmission_id=transmission.pk
                                                             )
                    change_transmission_status = mailing.models.Transmission.objects.get(id=transmission.pk)
                    change_transmission_status.status = "READY"
                    change_transmission_status.save()

            # WEEKLY
            today = datetime.today().weekday()
            if transmission.frequency == "WEEKLY":
                print("TYPE: SEND WEEKLY")
                print("ID:", transmission.pk)
                convert_time = str(transmission.time)[:5]
                print("TIME:", convert_time)
                message = transmission.get_messages()
                print("MESSAGE THEME:", message.theme)
                print("MESSAGE BODY:", message.body)
                for client_mail in transmission.get_clients():
                    print("EMAIL:", client_mail.email)
                    emails_base.append(client_mail.email)
                    print(emails_base)

                    if today == 0:
                        schedule.every().sunday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)
                    if today == 1:
                        schedule.every().monday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)
                    if today == 2:
                        schedule.every().tuesday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)
                    if today == 3:
                        schedule.every().wednesday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)
                    if today == 4:
                        schedule.every().thursday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)
                    if today == 5:
                        schedule.every().friday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)
                    if today == 6:
                        schedule.every().saturday.at(convert_time).do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)

                    change_transmission_status = mailing.models.Transmission.objects.get(id=transmission.pk)
                    change_transmission_status.status = "READY"
                    change_transmission_status.save()

            # MONTHLY
            if transmission.frequency == "MONTHLY":
                print("TYPE: SEND MONTHLY")
                print("ID:", transmission.pk)
                convert_time = str(transmission.time)[:5]
                print("TIME:", convert_time)
                message = transmission.get_messages()
                print("MESSAGE THEME:", message.theme)
                print("MESSAGE BODY:", message.body)
                for client_mail in transmission.get_clients():
                    print("EMAIL:", client_mail.email)
                    emails_base.append(client_mail.email)
                    print(emails_base)
                    schedule.every(4).weeks.do(sendmail_after, emails_base=emails_base, message_theme=message.theme, message_body=message.body, transmission_id=transmission.pk)

                    change_transmission_status = mailing.models.Transmission.objects.get(id=transmission.pk)
                    change_transmission_status.status = "READY"
                    change_transmission_status.save()

            print("----------------------------------------------------")
            print(schedule.get_jobs())

        while True:
            schedule.run_pending()
            time.sleep(1)

    return render(request, "mailing/run_scheduler.html")
