from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def show_data(request):
    print(("*") * 30)
    print("Got data from survey!")
    print(request.POST)
    name = request.POST['name']
    location = request.POST['location']
    language = request.POST['language']
    comment = request.POST['comment']
    if request.POST['comment']:
        comment = request.POST['comment']
    else:
        comment = "No comment was provided!"
    context = {
        'nameTemplate': name,
        'locationTemplate': location,
        'languageTemplate': language,
        'commentTemplate': comment,
    }
    return render(request, "show.html", context)
