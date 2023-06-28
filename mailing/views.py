# from datetime import datetime
from datetime import datetime, timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailing.models import Messages, Clients, Transmission
from mailing.utils import sendmail
from mailing.forms import TransmissionCreateForm, Statistic
import pytz


class MainView(ListView):
    model = Messages
    template_name = "mailing/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main"
        return context


class ClientsView(ListView):
    model = Clients
    template_name = "mailing/clients.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Clients"
        context["Clients"] = Clients.objects.all()
        return context


class ClientsCreate(CreateView):
    model = Clients
    template_name = "mailing/client_create.html"
    fields = ["full_name", "email", "comment"]

    def get_context_data(self, *, object_list=None, context_object_name=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Add New Client"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:clients')


class ClientsDelete(DeleteView):
    model = Clients
    template_name = "mailing/delete.html"

    def get_context_data(self, *, object_list=None, context_object_name=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Client"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:clients')


class MessagesView(ListView):
    model = Messages
    template_name = "mailing/messages.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Messages"
        context["Messages"] = Messages.objects.all()
        return context


class MessageCreate(CreateView):
    model = Messages
    template_name = "mailing/message_create.html"
    fields = ["theme", "body"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Create Message Template"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:messages')


class MessageDelete(DeleteView):
    model = Messages
    template_name = "mailing/delete.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Message"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:messages')


class TransmissionCard(DetailView):
    model = Transmission
    template_name = "mailing/transmission_card.html"
    slug_url_kwarg = "transmission_slug"

    def get_object(self, queryset=None):
        one_transmission = super().get_object()
        return one_transmission

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Transmission Full Information"
        current_object = self.get_object()
        print(current_object.owner)
        context["Transmission"] = current_object
        context["Statistic"] = current_object.get_statistic[0]
        print(current_object.get_statistic[0])
        return context


class TransmissionView(ListView):
    model = Transmission
    template_name = "mailing/transmissions.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Transmissions"
        context["Transmissions"] = Transmission.objects.all()
        return context


class TransmissionCreate(CreateView):
    model = Transmission
    form_class = TransmissionCreateForm
    template_name = "mailing/transmission_create.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Create New Transmission"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:transmissions')

    def form_valid(self, form):

        # Create default data statistic
        current_transmission = self.object
        print(current_transmission)
        print("---------------------------------------------------------")
        self.object = form.save()

        # save owner of transmission
        self.object.owner = self.request.user
        self.object.save()

        # Set default data for created transmission
        Statistic.objects.create(transmission_id=self.object.pk)
        # Executing send message
        schedule_transmission_time = self.object.time
        current_time = datetime.now().time()
        print(schedule_transmission_time, current_time)

        if schedule_transmission_time <= current_time:
            send_message = self.object.message.get_info()
            print("!SEND MESSAGE!")
            for client in self.object.clients.all():

                print(client.email)
                print(client)
                sendmail(client.email, send_message[0], send_message[1])
            current_time = datetime.now(pytz.timezone('Europe/Moscow'))
            print(current_time)
            wu = Statistic.objects.get(transmission_id=self.object.pk)
            wu.status = "FINISHED"
            wu.mail_answer = "OK"
            wu.time = datetime.now(pytz.timezone('Europe/Moscow'))
            wu.save()

        return super().form_valid(form)


class TransmissionDelete(DeleteView):
    model = Transmission
    template_name = "mailing/delete.html"
    slug_url_kwarg = "transmission_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Transmission"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:transmissions')



