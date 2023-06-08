import datetime
from django.db import models


class Clients(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="client name", null=False, blank=False)
    comment = models.TextField(max_length=500, null=True, blank=True, verbose_name="comment about client")
    email = models.EmailField(max_length=255,  verbose_name="client mail", null=False, blank=False)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.full_name}"


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
    time = models.DateTimeField(verbose_name="start time for sending", default=datetime.datetime(2023, 1, 1))
    # time = models.DateTimeField(verbose_name="start time for sending", default=datetime.time)
    frequency = models.CharField(choices=TransmissionFrequency.choices)
    status = models.CharField(choices=TransmissionStatus.choices, default=TransmissionStatus.Created)
    message = models.ForeignKey("Messages", on_delete=models.SET_NULL, null=True, blank=True)
    clients = models.ManyToManyField("Clients")
    statistic = models.OneToOneField("Statistic", on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Transmission"
        verbose_name_plural = "Transmission Templates"

    def __str__(self):
        return f"Transmission: {self.title}"


class Messages(models.Model):
    theme = models.CharField(max_length=50, verbose_name="message theme", null=False, blank=False)
    body = models.TextField(max_length=500, verbose_name="message body", null=False, blank=False)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"Message: {self.theme}"


class Statistic(models.Model):

    class AttemptStatus(models.TextChoices):
        Finished = 'FINISHED'
        Created = 'CREATED'

    time = models.DateTimeField(verbose_name="last time for send", default=None, null=True, blank=True)
    status = models.CharField(choices=AttemptStatus.choices, default=AttemptStatus.Created)
    mail_answer = models.CharField(verbose_name="answer from mailserver", default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Statistic"
        verbose_name_plural = "Statistics"

    def __str__(self):
        return f"{self.status} | {self.time} | {self.mail_answer}"
