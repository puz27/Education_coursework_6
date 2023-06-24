from mailing.utils import sendmail

def my_scheduled_job():
  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
  sendmail("n.avramenko87@yandex.ru", "TEST", "TEST")




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
