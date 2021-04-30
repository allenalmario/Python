from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

# Create your views here.
def homePage(request):
    return render(request, "index.html")

def wall(request):
    if 'loggedIn' in request.session:
        context = {
            'messages': Message.objects.all(),
        }
        return render(request, "wall.html", context)
    else:
        return redirect('/')

def post(request):
    thisUser = User.objects.filter(id=request.session['userID'])
    Message.objects.create(message=request.POST['postMessage'],user=thisUser[0])
    return redirect('/wall')

def comment(request, num):
    thisMessage = Message.objects.get(id=num)
    commentPoster = User.objects.get(id=request.session['userID'])
    Comment.objects.create(comment=request.POST['postComment'], message=thisMessage, user=commentPoster)
    print("Successfully posted comment!")
    return redirect('/wall')

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
        this_user = User.objects.get(id=user[0].id)
        request.session['usersName'] = this_user.firstName
        request.session['userID'] = this_user.id
        return redirect('/wall')

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
                this_user = User.objects.get(id=targetUser[0].id)
                request.session['usersName'] = this_user.firstName
                request.session['userID'] = this_user.id
                return redirect('/wall')
            else:
                messages.error(request, "Invalid login credentials, please try again")
                return redirect('/')

def logOut(request):
    del request.session['loggedIn']
    del request.session['usersName']
    del request.session['userID']
    return redirect('/')