from django.urls import path
from blog.views import BlogCard

app_name = "blog"

urlpatterns = [
    path("blog_card/<slug:blog_slug>", BlogCard.as_view(), name="blog_card"),
]
