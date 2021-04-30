from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, "login.html")

def register(request):
    # Register User
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE register FUNCTION!")
    print("*"*70)
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        newUser = User.objects.create(firstName=request.POST['firstName'],lastName=request.POST['lastName'],email=request.POST['email'],password=hashed_password)
        request.session['userID'] = newUser.id
        return redirect('/books')

def login(request):
    # Login Validator
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE login FUNCTION!")
    print("*"*70)
    errors = {}
    targetUser = User.objects.filter(email=request.POST['loginEmail'])
    if targetUser:
        logged_user = targetUser[0]
        if bcrypt.checkpw(request.POST['loginPassword'].encode(), logged_user.password.encode()):
            request.session['userID'] = logged_user.id
            return redirect('/books')
        else:
            messages.error(request, "Invalid login credentials, please try again")
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
    else:
        messages.error(request, "Email doesn't exist, please register")
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

def home(request):
    # Render Home page
    if 'userID' in request.session:
        books = Book.objects.all()
        current_user = User.objects.filter(id=request.session['userID'])
        context = {
            'books': books,
            'user': current_user[0],
        }
        return render(request, 'home.html',context)
    else:
        return redirect("/")

def addFavBook(request):
    # Add favorite book
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE addFavBook FUNCTION!")
    print("*"*70)
    errors = Book.objects.book_validator(request.POST)
    user = User.objects.filter(id=request.session['userID'])
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books')
    else:
        newBook = Book.objects.create(title=request.POST['bookTitle'], desc=request.POST['bookDesc'], uploaded_by=user[0])
        newBook.users_who_like.add(user[0])
        print("*"*70)
        print("SUCCESSFULlY ADDED FAVORITE BOOK")
        print("*"*70)
        return redirect('/books')

def renderBook(request, book_id):
    if 'userID' in request.session:
        book = Book.objects.filter(id=book_id)
        current_user = User.objects.filter(id=request.session['userID'])
        context = {
            'book': book[0],
            'user': current_user[0],
        }
        return render(request, 'book.html', context)
    else:
        return redirect('/')

def update(request, book_id):
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE update FUNCTION!")
    print("*"*70)
    errors = Book.objects.edit_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/books/{book_id}')
    else:
        bookToEdit = Book.objects.get(id=book_id)
        bookToEdit.title = request.POST['titleToEdit']
        bookToEdit.desc = request.POST['descToEdit']
        bookToEdit.save()
        print("*"*70)
        print("SUCCESSFULlY EDITED BOOK")
        print("*"*70)
        print(bookToEdit.title)
        print(bookToEdit.desc)
        return redirect(f'/books/{book_id}')

def delete(request, book_id):
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE delete FUNCTION!")
    print("*"*70)
    bookToDelete = Book.objects.get(id=book_id)
    bookToDelete.delete()
    return redirect(f'/books')

def addToFav(request, book_id):
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE addToFav FUNCTION!")
    print("*"*70)
    bookToAdd = Book.objects.filter(id=book_id)
    current_user = User.objects.filter(id=request.session['userID'])
    current_user[0].liked_books.add(bookToAdd[0])
    print("*"*70)
    print("SUCCESSFULLY ADDED BOOK TO FAVORITES!")
    print("*"*70)
    return redirect(f'/books/{book_id}')

def unfav(request, book_id):
    print("*"*70)
    print("SUCCESSFULLY GETTING TO THE unfav FUNCTION!")
    print("*"*70)
    bookToUnfav = Book.objects.filter(id=book_id)
    current_user = User.objects.filter(id=request.session['userID'])
    current_user[0].liked_books.remove(bookToUnfav[0])
    print("*"*70)
    print("SUCCESSFULLY REMOVED BOOK FROM FAVORITES!")
    print("*"*70)
    return redirect(f'/books/{book_id}')

def clearSession(request):
    # Logs user out and clears session
    request.session.clear()
    return redirect('/')