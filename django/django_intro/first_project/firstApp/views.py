from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["bruce", "fitz", "Georgie"]
    }
    return render(request, "index.html", context)
