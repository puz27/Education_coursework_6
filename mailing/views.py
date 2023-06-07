from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailing.models import Messages, Clients, Transmission


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
        return reverse_lazy('clients')


# class ClientsDelete(DeleteView):
#     model = Clients
#     template_name = "mailing/client_create.html"
#
#     def get_context_data(self, *, object_list=None, context_object_name=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["Title"] = "Delete Client"
#         return context
#
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('clients')


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
        return reverse_lazy('messages')


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
    template_name = "mailing/transmission_create.html"
    fields = ["title", "time", "frequency", "message", "clients"]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Create New Transmission"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('transmissions')


class TransmissionDelete(DeleteView):
    model = Transmission
    template_name = "mailing/transmission_delete.html"
    # slug_url_kwarg = "update_slug"
    pk_url_kwarg = "pk"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Transmission"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('transmissions')



