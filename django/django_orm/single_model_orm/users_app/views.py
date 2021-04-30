from django.shortcuts import render, redirect
from .models import User
# Create your views here.
def index(request):
    context = {
        "Users": User.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    fname = request.POST["first_name"] 
    lname = request.POST["last_name"]
    email = request.POST["email"]
    age = int(request.POST["age"])
    User.objects.create(first_name=fname, last_name=lname, email_address=email, age=age)
    return redirect('/')