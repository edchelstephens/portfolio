from django.urls import path

from pages.views import contact, page

app_name = "pages"

urlpatterns = [
    path("", page.IndexView.as_view(), name="index"),
    path("contact-me-email/", contact.ContactMeEmailView.as_view()),
]
