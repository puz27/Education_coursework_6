from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailing.models import Messages, Clients, Transmission
from mailing.services import sendmail
from mailing.forms import TransmissionCreateForm, Statistic, ClientCreateForm, MessageCreateForm
import pytz
from blog.models import Blog
import schedule


class MainView(LoginRequiredMixin, ListView):
    model = Messages
    template_name = "mailing/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main"
        # show blogs
        context["Blog"] = Blog.objects.order_by('?')[:3]
        # show statistic
        context["all_transmissions"] = len(Transmission.objects.all())
        context["active_transmissions"] = len(Transmission.objects.filter(is_published=True))
        context["all_clients"] = len(Clients.objects.all())
        context["unique_clients"] = len(Clients.objects.all().values('email').distinct())
        return context


class ClientsView(ListView):
    model = Clients
    template_name = "mailing/clients.html"

    def get_queryset(self):
        queryset = super().get_queryset().all()

        if not self.request.user.is_staff:
            queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Clients"
        context["Clients"] = self.get_queryset()
        return context


class ClientCard(DetailView):
    model = Clients
    template_name = "mailing/client_card.html"
    slug_url_kwarg = "client_slug"

    def get_object(self, queryset=None):
        one_client = super().get_object()
        return one_client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Client Full Information"
        context["Client"] = self.get_object()
        return context


class ClientCreate(CreateView):
    model = Clients
    form_class = ClientCreateForm
    template_name = "mailing/client_create.html"

    def get_context_data(self, *, object_list=None, context_object_name=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Add New Client"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:clients')

    def form_valid(self, form):
        def job():
            print("I'm working...")

        schedule.every(1).minutes.do(job)
        schedule.run_pending()


        # save owner of user
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdate(UpdateView):
    """Update client."""
    model = Clients
    fields = ["full_name", "comment", "email"]
    template_name = "mailing/client_update.html"
    slug_url_kwarg = "client_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Client"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:clients')

    def form_valid(self, form):
        return super().form_valid(form)


class ClientDelete(DeleteView):
    model = Clients
    template_name = "mailing/delete.html"
    slug_url_kwarg = "client_slug"

    def get_context_data(self, *, object_list=None, context_object_name=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Client"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:clients')


class MessagesView(ListView):
    model = Messages
    template_name = "mailing/messages.html"

    def get_queryset(self):
        queryset = super().get_queryset().all()

        if not self.request.user.is_staff:
            queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Messages"
        context["Messages"] = self.get_queryset
        return context


class MessageCard(DetailView):
    model = Messages
    template_name = "mailing/message_card.html"
    slug_url_kwarg = "message_slug"

    def get_object(self, queryset=None):
        one_message = super().get_object()
        return one_message

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Message Full Information"
        context["Message"] = self.get_object()
        return context


class MessageCreate(CreateView):
    model = Messages
    template_name = "mailing/message_create.html"
    form_class = MessageCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Create Message Template"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:messages')

    def form_valid(self, form):
        # save owner of message
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdate(UpdateView):
    """Update message."""
    model = Messages
    fields = ["theme", "body"]
    template_name = "mailing/message_update.html"
    slug_url_kwarg = "message_slug"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Message"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:messages')

    def form_valid(self, form):
        return super().form_valid(form)


class MessageDelete(DeleteView):
    model = Messages
    template_name = "mailing/delete.html"
    slug_url_kwarg = "message_slug"

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

    def get_queryset(self):
        queryset = super().get_queryset().all()

        if not self.request.user.is_staff:
            queryset = super().get_queryset().filter(owner=self.request.user)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Transmissions"
        # context["Transmissions"] = Transmission.objects.filter(owner=self.request.user)
        context["Transmissions"] = self.get_queryset()
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
            print("!SEND MESSAGE NOW!")
            for client in self.object.clients.all():
                print(client)
                sendmail(client.email, send_message[0], send_message[1])
            # current_time = datetime.now(pytz.timezone('Europe/Moscow'))
            statistic = Statistic.objects.get(transmission_id=self.object.pk)
            statistic.status = "FINISHED"
            statistic.mail_answer = "OK"
            statistic.time = datetime.now(pytz.timezone('Europe/Moscow'))
            statistic.save()

            self.object.status = "FINISHED"
            self.object.save()


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


class TransmissionUpdate(UpdateView):
    """Update product."""
    model = Transmission
    fields = ["title", "time", "frequency", "message", "clients", "is_published"]
    template_name = "mailing/transmission_update.html"
    slug_url_kwarg = "transmission_slug"
    # permission_required = ("catalog.view_product")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Update Transmission"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:transmissions')

    def form_valid(self, form):

        # check send time
        schedule_transmission_time_update = form.cleaned_data["time"]
        current_time = datetime.now().time()
        print(schedule_transmission_time_update, current_time)

        if schedule_transmission_time_update <= current_time:
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
