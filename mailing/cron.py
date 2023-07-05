from mailing.services import sendmail


def my_scheduled_job():
    sendmail("n.avramenko87@yandex.ru", "TEST", "TEST")
    sendmail("n.avramenko87@gmail.ru", "TEST", "TEST")

    print("HELLO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINUTES = 1
#     RUN_AT_TIMES = ['23:42']
#     schedule = Schedule(run_at_times=RUN_AT_TIMES)
#     code = "mailing.utils.MyCronJob"
#
#     def do_work(self):
#
#         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
#
