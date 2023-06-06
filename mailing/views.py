from django.shortcuts import render


def main_page(request):
    context = {"Title": "Title!!!"}
    return render(request, "mailing/main.html", context)


def messages_create(request):
    context = {"Title": "Message!!!"}
    return render(request, "mailing/messages.html", context)


def user_create(request):
    return render(request, "mailing/main.html")
