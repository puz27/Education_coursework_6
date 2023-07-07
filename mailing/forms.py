from django import forms
from mailing.models import Transmission, Statistic, Clients, Messages


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_published":
                field.widget.attrs["class"] = "form-control"


class TransmissionCreateForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["message"].empty_label = "Select Message"

    class Meta:
        model = Transmission
        fields = ["title", "time", "frequency", "message", "clients"]


class ClientCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Clients
        fields = ["full_name", "email", "comment"]


class MessageCreateForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Messages
        fields = ["theme", "body"]


class StatisticForm(forms.ModelForm):

    class Meta:
        model = Statistic
        fields = ["time", "status", "mail_answer"]
