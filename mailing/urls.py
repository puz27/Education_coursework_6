from django.urls import path
from mailing.views import MessagesView, ClientsView, MainView, ClientsCreate, MessageCreate, TransmissionCreate,\
    TransmissionView, TransmissionDelete, MessageDelete, ClientsDelete

app_name = "mailing"


urlpatterns = [
    path("", MainView.as_view(), name="main_page"),
    path("messages/", MessagesView.as_view(), name="messages"),
    path("message_create/", MessageCreate.as_view(), name="message_create"),
    path("message_delete/<int:pk>", MessageDelete.as_view(), name="message_delete"),
    path("clients/", ClientsView.as_view(), name="clients"),
    path("client_create/", ClientsCreate.as_view(), name="client_create"),
    path("client_delete/<int:pk>", ClientsDelete.as_view(), name="client_delete"),
    path("transmissions/", TransmissionView.as_view(), name="transmissions"),
    path("transmission_create/", TransmissionCreate.as_view(), name="transmission_create"),
    path("transmission_delete/<int:pk>", TransmissionDelete.as_view(), name="transmission_delete"),
]
