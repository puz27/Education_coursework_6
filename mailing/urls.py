from django.urls import path
from mailing.views import main_page, messages_create, user_create

urlpatterns = [
    path("", main_page, name="main_page"),
    path("messages/", messages_create, name="messages"),
    path("users/", user_create, name="users"),
]