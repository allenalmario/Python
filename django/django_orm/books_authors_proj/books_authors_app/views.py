from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        "all_books": books,
    }
    return render(request, "index.html", context)

def authors(request):
    authors = Author.objects.all()
    context = {
        "all_authors": authors,
    }
    return render(request, "authors.html", context)

def addBook(request):
    book_title = request.POST["bookTitle"]
    book_desc = request.POST["desc"]
    Book.objects.create(title=book_title, desc=book_desc)
    return redirect("/")

def addAuthor(request):
    author_fname = request.POST["fname"]
    author_lname = request.POST["lname"]
    author_notes = request.POST["notes"]
    Author.objects.create(first_name=author_fname, last_name=author_lname, notes=author_notes)
    return redirect("/authors")

def renderBook(request, num):
    specific_instance = Book.objects.get(id=num)
    authors = Author.objects.all()
    context = {
        "specificBook": specific_instance,
        "authors": authors,
    }
    return render(request, "showBook.html", context)

def addAuthorToBook(request):
    author = request.POST["author"]
    book = request.POST["book"]
    bookToAddTo = Book.objects.get(id=book)
    authorToAdd = Author.objects.get(id=author)
    bookToAddTo.authors.add(authorToAdd)
    return redirect(f'books/{book}')

def renderAuthor(request, num):
    specific_author = Author.objects.get(id=num)
    books = Book.objects.all()
    context = {
        "specificAuthor": specific_author,
        "books": books,
    }
    return render(request, "showAuthor.html", context)

def addBookToAuthor(request):
    book = request.POST["book"]
    author = request.POST["author"]
    authorToAddTo = Author.objects.get(id=author)
    bookToAdd = Book.objects.get(id=book)
    authorToAddTo.books.add(bookToAdd)
    return redirect(f'authors/{author}')