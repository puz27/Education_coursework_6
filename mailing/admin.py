from django.contrib import admin
from mailing.models import Client, Transmission, Message, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "comment")
    search_fields = ("full_name", "email")
    list_filter = ("full_name", "email")
    # prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Transmission)
class Transmission(admin.ModelAdmin):
    pass


@admin.register(Message)
class Message(admin.ModelAdmin):
    list_display = ("theme",)
    search_fields = ("theme",)
    list_filter = ("theme",)
    # prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Attempt)
class Attempt(admin.ModelAdmin):
   pass

