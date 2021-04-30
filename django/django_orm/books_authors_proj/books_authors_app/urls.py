from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addBook', views.addBook),
    path('authors', views.authors),
    path('addAuthor', views.addAuthor),
    path('books/<int:num>', views.renderBook),
    path('addAuthorToBook', views.addAuthorToBook),
    path('authors/<int:num>', views.renderAuthor),
    path('addBookToAuthor', views.addBookToAuthor),
]