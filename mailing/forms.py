# from django import forms
# from mailing.models import Transmission
# from django.contrib.admin import widgets
#
#
# class TransmissionForm(forms.ModelForm):
#     class Meta:
#         model = Transmission
#
#     def __init__(self, *args, **kwargs):
#         super(TransmissionForm, self).__init__(*args, **kwargs)
#         self.fields['mydate'].widget = widgets.AdminDateWidget()
#         self.fields['mytime'].widget = widgets.AdminTimeWidget()
#         self.fields['mydatetime'].widget = widgets.AdminSplitDateTime()