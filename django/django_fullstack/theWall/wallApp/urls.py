from django.urls import path
from . import views

urlpatterns = [
    # render or GET routes
    path('', views.homePage),
    path('wall', views.wall),
    path('logOut', views.logOut),

    # POST routes
    path('register', views.register),
    path('logIn', views.logIn),
    path('post', views.post),
    path('comment/<int:num>', views.comment),
]