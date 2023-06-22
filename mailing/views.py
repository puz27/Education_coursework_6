from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mailing.models import Messages, Clients, Transmission
from mailing.utils import sendmail
from mailing.forms import TransmissionForm, Statistic


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
        return reverse_lazy('mailing:clients')


class ClientsDelete(DeleteView):
    model = Clients
    template_name = "mailing/delete.html"

    def get_context_data(self, *, object_list=None, context_object_name=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Delete Client"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:clients')


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
        return reverse_lazy('mailing:messages')


class MessageDelete(DeleteView):
    model = Messages
    template_name = "mailing/delete.html"

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
        context["Transmission"] = current_object
        context["Statistic"] = current_object.get_statistic[0]
        return context


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
    form_class = TransmissionForm
    template_name = "mailing/transmission_create.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Create New Transmission"
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('mailing:transmissions')

    def form_valid(self, form):

        # default_statistic = Statistic.objects.create(transmission=7)
        print(form)
        self.object = form.save()
        current_pk = self.object
        print(current_pk)
        print("---------------------------------------------------------")
        self.object = form.save()
        send_message = self.object.message.get_info()
        # send_time = self.object.
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        for client in self.object.clients.all():
            print(client.email)
            sendmail(client.email, send_message[0], send_message[1])
        return super().form_valid(form)


# class TransmissionCreate(View):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'mailing/transmission_create.html', {'form': CreateTransmissionForm(), })
#
#     def post(self, request, *args, **kwargs):
#         form = CreateTransmissionForm(data=request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             frequency = form.cleaned_data['frequency']
#             status = form.cleaned_data['status']
#             message = form.cleaned_data['message']
#             date = form.cleaned_data.get('date')
#             time = form.cleaned_data.get('time')
#             clients = form.cleaned_data['clients']
#             obj = Transmission.objects.create(title=title,
#                                               date=date,
#                                               time=time,
#                                               frequency=frequency,
#                                               status=status,
#                                               message=message,
#                                               clients=object.set(clients))
#             obj.save()
#             # return redirect('transmissions', pk=obj.pk)
#
#         return self.get(request)



    # def post(self, request, *args, **kwargs):
    #     form = TaskForm(data=request.POST)
    #     if form.is_valid():
    #         task = form.save()
    #         return redirect('task-detail', pk=task.pk)
    #
    #     return self.get(request)


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



