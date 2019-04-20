from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .utils import scrape

# Create your views here.
def index(request):
    data = scrape()
    context = {
        "data": data
    }
    return render(request, "home/index.html", context)
