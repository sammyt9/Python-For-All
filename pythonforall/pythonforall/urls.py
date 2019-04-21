"""pythonforall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# We Christian Cabauatan and Sammy Tieng have contributed equally to this project.
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
import home.views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    url(r'^mplpie.png$', home.views.mplpie),
    url(r'^mplbar.png$', home.views.mplbar),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
