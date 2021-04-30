from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    if 'gold' in request.session:
        pass
    else:
        request.session['gold'] = 0
    if 'list' in request.session:
        pass
    else:
        request.session['list'] = []
    return render(request, "index.html")

def process_money(request):
    if request.POST['which_form'] == 'farm':
        # do farm process
        farmGold = random.randint(10, 20)
        request.session['gold'] += farmGold
        request.session['list'].append(f"Earned {farmGold} golds from the Farm!")
        request.session.save()
        return redirect("/")
    elif request.POST['which_form'] == 'cave':
        # do cave process
        caveGold = random.randint(5, 10)
        request.session['gold'] += caveGold
        request.session['list'].append(f"Earned {caveGold} golds from the Cave!")
        request.session.save()
        return redirect("/")
    elif request.POST['which_form'] == 'house':
        # do house process
        houseGold = random.randint(2, 5)
        request.session['gold'] += houseGold
        request.session['list'].append(f"Earned {houseGold} golds from the House!")
        request.session.save()
        return redirect("/")
    elif request.POST['which_form'] == 'casino':
        # do casino process
        chance = random.randint(1,2)
        casinoGold = random.randint(0, 50)
        if chance == 1:
            request.session['gold'] -= casinoGold
            request.session['list'].append(f"Lost {casinoGold} golds from the Casino... ouch!")
            request.session.save()
        elif chance == 2:
            request.session['gold'] += casinoGold
            request.session['list'].append(f"Won {casinoGold} golds from the Casino! YAY!")
            request.session.save()
        return redirect("/")