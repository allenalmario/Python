from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    print("*"*40)
    randNum = random.randint(1, 100)
    # print(f"Randomly generated number: {randNum}")
    request.session['randomNumber'] = randNum
    return render(request, "index.html")

def guess(request):
    # print("*"*40)
    # print("Got to the 'guess' function!")
    num = int(request.POST['number'])
    if 'tries' in request.session:
        request.session['tries'] += 1
    else:
        request.session['tries'] = 1
    # print(f"got number {num}")
    # print(f"Randomly generated number: {request.session['randomNumber']}")
    context = {
        'number' : num,
        'random' : request.session['randomNumber'],
        'tries' : request.session['tries'],
    }
    return render(request, "result.html", context)

def replay(request):
    del request.session['tries']
    return redirect(index)