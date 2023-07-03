import datetime
from config import settings

import django as django
from django.db import models
from mailing.utils import d_slugify


class Clients(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="client name", null=False, blank=False)
    comment = models.TextField(max_length=500, null=True, blank=True, verbose_name="comment about client")
    email = models.EmailField(max_length=255,  verbose_name="client mail", null=False, blank=False)
    slug = models.SlugField(max_length=255, verbose_name="client slug", null=False, unique=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = d_slugify(self.full_name)
        super().save(*args, **kwargs)


class Transmission(models.Model):

    class TransmissionStatus(models.TextChoices):
        Finished = 'FINISHED'
        Created = 'CREATED'
        Running = 'RUNNING'

    class TransmissionFrequency(models.TextChoices):
        Daily = 'DAILY'
        Weekly = 'WEEKLY'
        Monthly = 'MONTHLY'

    title = models.CharField(max_length=100, verbose_name="transmission name", null=False, blank=False, unique=True)
    # time = models.DateTimeField(verbose_name="start time for sending", default=datetime.datetime(2023, 1, 1))
    # time = models.TimeField(verbose_name="start time for sending", default=datetime.datetime.now().time())
    time = models.TimeField(verbose_name="start time for sending", default=django.utils.timezone.now)
    frequency = models.CharField(choices=TransmissionFrequency.choices)
    status = models.CharField(choices=TransmissionStatus.choices, default=TransmissionStatus.Created)
    message = models.ForeignKey("Messages", on_delete=models.SET_NULL, null=True, blank=True)
    clients = models.ManyToManyField("Clients")
    slug = models.SlugField(max_length=255, verbose_name="transmission slug", null=False, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Transmission"
        verbose_name_plural = "Transmission Templates"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = d_slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Transmission: {self.title}"

    @property
    def get_statistic(self):
        return self.statistic_of_transmission.all()


class Messages(models.Model):
    theme = models.CharField(max_length=50, verbose_name="message theme", null=False, blank=False)
    body = models.TextField(max_length=500, verbose_name="message body", null=False, blank=False)
    slug = models.SlugField(max_length=255, verbose_name="message slug", null=False, unique=True)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.theme, self.body}"

    def get_info(self):
        """Return information for sending to client"""
        return self.theme, self.body

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = d_slugify(self.theme)
        super().save(*args, **kwargs)


class Statistic(models.Model):

    class AttemptStatus(models.TextChoices):
        Finished = 'FINISHED'
        Created = 'CREATED'

    transmission = models.ForeignKey("Transmission", on_delete=models.CASCADE, related_name="statistic_of_transmission")
    time = models.DateTimeField(verbose_name="last time for send", default=None, null=True, blank=True)
    status = models.CharField(choices=AttemptStatus.choices, default=AttemptStatus.Created)
    mail_answer = models.CharField(verbose_name="answer from mailserver", default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"Status: {self.status} Time: {self.time} Mail answer: {self.mail_answer}"
