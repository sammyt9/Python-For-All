from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from .utils import scrape
from .utils import parseData

# Create your views here.
def index(request):
    data = scrape()
    context = {
        "data": data
    }
    return render(request, "home/index.html", context)

def mplimage(request):
    labels = ['AI/Deep Learning', 'Data Science', 'Learning/Tips', 'Web Scraping', 'Misc']
    data = scrape()
    data_results = parseData(data)
    np_results = np.zeros(5)
    i = 0
    for key, value in data_results.items():
        np_results[i] = value
        i += 1
    fig = Figure(facecolor='white')
    ax = fig.add_subplot(111, aspect='equal')
    ax.pie(np_results, labels=labels)
    ax.set_title('Python Topic Statistics')
    canvas = FigureCanvas(fig)
    request = HttpResponse(content_type='image/png')
    canvas.print_png(request)
    return request