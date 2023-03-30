from django.shortcuts import render


def index(request):
    """Index page view."""
    return render(request, "pages/index.html")
