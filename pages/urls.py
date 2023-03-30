from django.urls import path

from pages.views import page

urlpatterns = [
    path("", page.index, name="index"),
]
