from django.contrib import admin
from mailing.models import Clients, Transmission, Messages, Statistic


@admin.register(Clients)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "comment")
    search_fields = ("full_name", "email")
    list_filter = ("full_name", "email")
    # prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    list_display = ("title", "time", "frequency", "status", "statistic")
    list_filter = ("status",)
    filter_horizontal = ["clients"]
    # prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("theme",)
    search_fields = ("theme",)
    list_filter = ("theme",)
    # prepopulated_fields = {"slug": ("full_name",)}


@admin.register(Statistic)
class AttemptAdmin(admin.ModelAdmin):
   list_display = ("time", "status", "mail_answer",)



