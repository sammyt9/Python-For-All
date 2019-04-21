from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from .utils import scrape
from .utils import parseData

data = scrape()

# Create your views here.
def index(request):
    # data = scrape()
    context = {
        "data": data
    }
    return render(request, "home/index.html", context)

def mplpie(request):
    labels = ['AI/Deep Learning', 'Data Science', 'Learning/Tips', 'Web Scraping', 'Misc']
    # data = scrape()
    data_results = parseData(data)
    np_results = np.zeros(5)
    i = 0
    for key, value in data_results.items():
        np_results[i] = value
        i += 1
    
    fig = Figure(facecolor='white')
    ax = fig.add_subplot(111, aspect='equal')
    ax.axis('equal')
    explode = (0.1, 0.1, 0.1, 0.1, 0.1)
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    pie = ax.pie(np_results, labels=labels, explode=explode, colors=colors, shadow=True, startangle=90)
    ax.set_title('Python Topics Statistics')
    fig.subplots_adjust(bottom=0.3, wspace=0.33)
    ax.legend(pie[0], labels, loc='center', bbox_to_anchor=(0.5, -0.2), ncol=2)
    canvas = FigureCanvas(fig)
    request = HttpResponse(content_type='image/png')
    canvas.print_png(request)
    return request

def mplbar(request):
    labels = ['AI/Deep Learning', 'Data Science', 'Learning/Tips', 'Web Scraping', 'Misc']
    data_results = parseData(data)
    np_results = np.zeros(5)
    i = 0
    for key, value in data_results.items():
        np_results[i] = value
        i += 1
    fig = Figure(figsize=(10, 10), facecolor='white')
    ax = fig.add_subplot(111)
    bar_width = 0.5
    colors = ['blue', 'orange', 'green', 'red', 'purple']
    bar = ax.bar(labels, np_results, bar_width, bottom=3, color=colors, align='center', alpha=0.5)
    ax.set_xlabel('Python Topics', fontsize=15)
    ax.set_ylabel('Number of Articles', fontsize=15)
    ax.set_title('Python Topics Statistics', fontsize=20)
    canvas = FigureCanvas(fig)
    request = HttpResponse(content_type='image/png')
    canvas.print_png(request)
    return request