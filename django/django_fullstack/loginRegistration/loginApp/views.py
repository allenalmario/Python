from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def homePage(request):
    return render(request, "index.html")

def success(request):
    if 'loggedIn' in request.session:
        return render(request, "welcome.html")
    else:
        return redirect('/')

def register(request):
    print("*"*50)
    print("REACHING register FUNCTION!")
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST['password']
        hashedPW = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(firstName=request.POST['first_name'],lastName=request.POST['last_name'],email=request.POST['email'],password=hashedPW)
        user = User.objects.filter(email=request.POST['email'])
        request.session['loggedIn'] = "Yes"
        request.session['user'] = user[0].firstName
        return redirect('/success')

def logIn(request):
    print("*"*50)
    print("REACHING logIn FUNCTION!")
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        targetUser = User.objects.filter(email = request.POST['loginEmail'])
        if not targetUser:
            messages.error(request, "User doesn't exist under that email, Please register!")
            return redirect('/')
        else:
            if bcrypt.checkpw(request.POST['loginPassword'].encode(), targetUser[0].password.encode()):
                request.session['loggedIn'] = "Yes"
                request.session['user'] = targetUser[0].firstName
                return redirect('/success')
            else:
                messages.error(request, "Invalid login credentials, please try again")
                return redirect('/')

def logOut(request):
    del request.session['loggedIn']
    del request.session['user']
    return redirect('/')