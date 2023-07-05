from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog


class BlogCard(DetailView):
    """Information about blog."""
    model = Blog
    template_name = "blog/blog_card.html"
    slug_url_kwarg = "blog_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Title"] = "Blog Information"
        current_object = self.get_object()
        context["Blog"] = current_object
        current_object.views += 1
        current_object.save()
        return context
