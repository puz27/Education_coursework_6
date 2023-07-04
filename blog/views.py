from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog


class BlogView(ListView):
    model = Blog
    template_name = "mailing/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Main"
        return context
