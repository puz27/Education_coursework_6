from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailing.models import Messages, Clients


class MainView(ListView):
    model = Messages
    template_name = "mailing/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main"
        return context


class ClientsView(ListView):
    model = Messages
    template_name = "mailing/clients.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Clients"
        context["Clients"] = Clients.objects.all()
        return context


class MessagesView(ListView):
    model = Messages
    template_name = "mailing/messages.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Messages"
        context["Messages"] = Messages.objects.all()
        return context
