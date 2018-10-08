from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('index', views.index, name = 'index'),
    path('results', views.results, name = 'results'),
    path('detail', views.detail, name = 'detail'),
 
]
