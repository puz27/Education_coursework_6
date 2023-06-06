from django.db import models


class Clients(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="client_name", null=False, blank=False)
    comment = models.CharField(max_length=100, verbose_name="comment_about_client", null=True, blank=True)
    email = models.EmailField(max_length=255, help_text="client name for mailing",  verbose_name="client_mail", null=False, blank=False)
    transmission = models.ManyToManyField("Transmission")

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

    title = models.CharField(max_length=100, verbose_name="transmission_name", null=False, blank=False, unique=True)
    time = models.DateTimeField(verbose_name="start_time_for_sending")
    frequency = models.CharField(choices=TransmissionFrequency.choices)
    status = models.CharField(choices=TransmissionStatus.choices, default=TransmissionStatus.Created)
    message = models.ForeignKey("Messages", on_delete=models.CASCADE)
    attempt = models.ForeignKey("Attempt", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Transmission"
        verbose_name_plural = "Transmission Templates"

    def __str__(self):
        return f"{self.time} {self.frequency} {self.status}"


class Messages(models.Model):
    theme = models.CharField(max_length=50, verbose_name="message_theme", null=False, blank=False)
    body = models.TextField(max_length=500, verbose_name="message_body", null=False, blank=False)

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return f"{self.theme}"


class Attempt(models.Model):

    class AttemptStatus(models.TextChoices):
        Finished = 'FINISHED'
        Created = 'CREATED'
        Running = 'RUNNING'

    time = models.DateTimeField(verbose_name="last_time_for_send", default=None, null=True, blank=True)
    status = models.CharField(choices=AttemptStatus.choices, default=AttemptStatus.Created)
    mail_answer = models.CharField(verbose_name="answer_from_mailserver", default=None, null=True, blank=True)

    class Meta:
        verbose_name = "Attempt"
        verbose_name_plural = "Attempts"

    def __str__(self):
        return f"{self.time} {self.status}"
