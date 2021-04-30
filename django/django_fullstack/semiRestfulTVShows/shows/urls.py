from django.urls import path
from . import views

urlpatterns = [
    path('', views.allShows),
    path('shows/new', views.addShowPage), # Add a New Show route
    path('processShow', views.addShowToDB), # Submit the data from the Add a New Show form
    path('shows', views.allShows), # All Shows route
    path('shows/<int:num>', views.showDetails), # Display show details on its own page route
    path('shows/<int:num>/edit', views.editShow), # Display edit form to edit show
    path('changeShowDetails', views.changeDetails), # submit the data from edit form
    path('shows/<int:num>/destroy', views.deleteShow),
]