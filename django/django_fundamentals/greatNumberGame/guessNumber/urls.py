from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('determine', views.guess),
    path('playAgain', views.replay)
]