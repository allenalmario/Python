from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from .models import Show # import the model to work with

# Create your views here.
def addShowPage(request):
    # this function will render "Add a New Show" page
    return render(request, "addNewShow.html")

def addShowToDB(request):
    # this function will add the submited show from "Add a New Show" page to the DataBase
    # and Redirect to the New Show's page
    errors = Show.objects.add_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        showToAddTitle = request.POST["showTitle"]
        showToAddNetwork = request.POST["showNetwork"]
        showToAddRD = request.POST["releaseDate"]
        showToAddDesc = request.POST["showDesc"]
        # A the new show to the Database by creating an instance of the Show model by using the data from request.POST
        Show.objects.create(title=showToAddTitle, network=showToAddNetwork, release_date=showToAddRD, desc=showToAddDesc)
        messages.success(request, "Show sucessfully added")
        # get the last instance in the show database cause the lastest show will always be the last
        addedShow = Show.objects.last()
        # take the id from the specific instance to redirect to
        addedShowID = addedShow.id
        return redirect(f'/shows/{addedShowID}')

def allShows(request):
    # This function will render the "All Shows" page
    showsFromDB = Show.objects.all()
    # Pass dictionary of all the shows to the allShows.html template
    context = {
        "shows": showsFromDB,
    }
    return render(request, "allShows.html", context)

def showDetails(request, num):
    #This function will render the "showDetails.html" page
    # Grab the specific show instance from the Database using the num parameter passed by the route
    specificShow = Show.objects.get(id=num)
    # send that information to template
    context = {
        "thisShow": specificShow
    }
    return render(request, "showDetails.html", context)

def editShow(request, num):
    # this function will render the "editForm.html" page
    # grab the specific show instance to edit
    showToEdit = Show.objects.get(id=num)
    # send that info to the template
    time = showToEdit.release_date
    dateStr = time.strftime("%Y-%m-%d")
    print(dateStr)
    context = {
        'editThisShow': showToEdit,
        'time': dateStr,
    }
    return render(request, "editForm.html", context)

def changeDetails(request):
    # This function will take in the edit form data and change the instances' details
    # grab show info by hidden input field from form
    showID = request.POST["id"]
    errors = Show.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{showID}/edit')
    else:
        titleToChange = request.POST["titleToEdit"]
        networkToChange = request.POST["networkToEdit"]
        rdToChange = request.POST["rdToEdit"]
        descToChange = request.POST["descToChange"]
        # Grab the specific show we're working with by grabbing the instance by its ID
        showDetailsToEdit = Show.objects.get(id=showID)
        # Change the values by grabbing each of the instances' attributes
        showDetailsToEdit.title = titleToChange
        showDetailsToEdit.network = networkToChange
        showDetailsToEdit.release_date = rdToChange
        showDetailsToEdit.desc = descToChange
        # Use the save function to save the changes made
        showDetailsToEdit.save()
        messages.success(request, "Show sucessfully edited")
        return redirect(f'/shows/{showID}')

def deleteShow(request, num):
    # grab the specific show's instance with id using parameter num
    showToDelete = Show.objects.get(id=num)
    showToDelete.delete() # deletes this instance from the database
    return redirect("/shows")