from django.urls import path
from . import views

urlpatterns = [
    # GET routes
    path('', views.index),
    path('books', views.home),
    path('books/<int:book_id>', views.renderBook),
    path('logout', views.clearSession),

    # POST routes
    path('register', views.register),
    path('login', views.login),
    path('addFavBook', views.addFavBook),
    path('books/update/<int:book_id>', views.update),
    path('books/<int:book_id>/delete', views.delete),
    path('addToFav/<int:book_id>', views.addToFav),
    path('unfav/<int:book_id>', views.unfav),
]