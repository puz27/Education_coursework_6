# from django import forms
# from django.forms import SelectDateWidget
#
# from mailing.models import Transmission, Messages, Clients
# from django.contrib.admin import widgets
#
#
# class CreateTransmissionForm(forms.Form):
#
#         title = forms.CharField(max_length=100)
#         frequency = forms.CharField()
#         status = forms.CharField()
#         message = forms.ModelChoiceField(queryset=Messages.objects.all())
#         clients = forms.ModelChoiceField(queryset=Clients.objects.all())
