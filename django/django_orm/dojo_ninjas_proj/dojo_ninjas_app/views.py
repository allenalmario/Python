from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all(),
    }
    return render(request, "index.html", context)

def processdojo(request):
    dojo_name = request.POST["name"]
    dojo_city = request.POST["city"]
    dojo_state = request.POST["state"]
    Dojo.objects.create(name=dojo_name, city=dojo_city, state=dojo_state)
    return redirect("/")

def processninja(request):
    ninja_fname = request.POST["fname"]
    ninja_lname = request.POST["lname"]
    dojo_id = request.POST["dojo"]
    dojo = Dojo.objects.get(id=dojo_id)
    Ninja.objects.create(dojo_id=dojo, first_name=ninja_fname, last_name=ninja_lname)
    return redirect("/")