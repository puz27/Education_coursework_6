from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from models import Messages


def main_page(request):
    context = {"Title": "Title!!!"}
    return render(request, "mailing/main.html", context)


def messages_create(request):
    context = {"Title": "Message!!!"}
    return render(request, "mailing/messages.html", context)


def user_create(request):
    return render(request, "mailing/main.html")


class Messages(ListView):
    model = Messages
    template_name = "mailing/messages.html"