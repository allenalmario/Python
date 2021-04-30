from django.urls import path
from . import views

urlpatterns = [
    # render routes
    path('', views.homePage),
    path('success', views.success),
    path('logOut', views.logOut),

    # POST routes
    path('register', views.register),
    path('logIn', views.logIn),
]