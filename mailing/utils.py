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





# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINUTES = 1
#     RUN_AT_TIMES = ['23:42']
#     schedule = Schedule(run_at_times=RUN_AT_TIMES)
#     code = "mailing.utils.MyCronJob"
#
#     def do_work(self):
#         sendmail("n.avramenko87@yandex.ru", "TEST", "TEST")
#         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1")
#
