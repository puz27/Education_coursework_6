from django.urls import path
from mailing.views import MessagesView, ClientsView, MainView

urlpatterns = [
    path("", MainView.as_view(), name="main_page"),
    path("messages/", MessagesView.as_view(), name="messages"),
    path("clients/", ClientsView.as_view(), name="clients"),
]
