from mailing.services import sendmail


def my_scheduled_job():
    sendmail("n.avramenko87@yandex.ru", "TEST", "TEST")
    sendmail("n.avramenko87@gmail.ru", "TEST", "TEST")
    print("HELLO!")

