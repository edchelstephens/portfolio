from django.http import HttpResponse
from django.shortcuts import render  # noqa


def index(request):
    """Index page view."""
    return HttpResponse("Pages index")
