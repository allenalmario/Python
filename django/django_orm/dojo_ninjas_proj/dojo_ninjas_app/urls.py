from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('processdojo', views.processdojo),
    path('processninja', views.processninja),
]