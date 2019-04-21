# We Christian Cabauatan and Sammy Tieng have contributed equally to this project.
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]