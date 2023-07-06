from mailing.services import sendmail
import schedule
import time


# def my_scheduled_job():
#     sendmail("n.avramenko87@yandex.ru", "TEST", "TEST")
#     sendmail("n.avramenko87@gmail.ru", "TEST", "TEST")
#
#     f = open('test.txt', 'w')
#     f.write('Hello \n World')
#     f.close()


# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINUTES = 1
#     RUN_AT_TIMES = ['23:42']
#     schedule = Schedule(run_at_times=RUN_AT_TIMES)
#     code = "mailing.utils.MyCronJob"
#
#     def do_work(self):
#
#         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")


def daily_task():
    print("Running daily task")


schedule.every().day.at("09:00").do(daily_task)
schedule.every(1).minutes.do(daily_task)

while True:
    schedule.run_pending()
    time.sleep(1)
