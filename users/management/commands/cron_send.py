from crontab import CronTab
from mailing.services import sendmail_after
from datetime import datetime
import pycron


# def set_cron():
#     with CronTab(user=True) as cron:
#         job = cron.new(command=sendmail_after)
#         job.minute.every(1)
#     print('cron.write() was just executed')


# @pycron.cron("* * * * * ")
# async def test(timestamp: datetime):
#     print(f"test cron job running at {timestamp}")
#
# if __name__ == '__main__':
#     pycron.start()
