from django.urls import path

from pages.views import page

app_name = "pages"

urlpatterns = [
    path("", page.index, name="index"),
]
