from django import forms
from mailing.models import Transmission, Statistic
# from django.forms import SelectDateWidget
#
# from mailing.models import Transmission, Messages, Clients
# from django.contrib.admin import widgets


class TransmissionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].empty_label = "Select Message"

    class Meta:
        model = Transmission
        fields = ["title", "time", "frequency", "message", "clients"]


class StatisticForm(forms.ModelForm):

    class Meta:
        model = Statistic
        fields = ["time", "status", "mail_answer"]
