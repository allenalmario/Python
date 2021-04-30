from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "day": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime())
    }
    return render(request,'index.html', context)