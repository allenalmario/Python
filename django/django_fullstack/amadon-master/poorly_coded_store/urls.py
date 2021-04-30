from django.urls import path
from . import views

urlpatterns = [
    path('amadon', views.index),
    path('processOrder', views.process),
    path('amadon/checkout', views.confirmation),
]
