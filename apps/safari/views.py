from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'safari/index.html')

def process(request):
    if len(request.POST['username']) < 1:
        messages.warning(request, "Username field can not be empty")
        return redirect('/')
    if request.session.get('username') == None:
        request.session['usename'] = request.POST['username']
        request.session['pokemon'] = []
        request.session['steps'] = 500
        request.session['time'] = 3000 # Five minutes? not sure how this will work yet.
        request.session['pokeballs'] = 99
        request.session['score'] = 0
        return render(request, 'safari/safari.html')

def area(request, zone):
    # Takes... 50 steps to go anywhere at the moment
    request.session['steps'] -= 50
    context = {
        'zone': zone
    }
    return render(request, 'safari/zone.html', context)

def pokemon(request, action):
    if action == 'grass':
        # Takes 20 steps to walk into grass
        request.session['steps'] -= 20
        # Logic for encountering random pokemon
        encounter = True
    if encounter == True:
        return render(request, 'safari/battle.html')
    # Not sure if we want to render battle.html if there is no encounter

def battlePokemon(request):
    if request.POST['action'] == 'bait':
        request.session['pokeballs'] += 0
        # Do something with bait
    elif request.POST['action'] == 'rock':
        request.session['pokeballs'] += 1
        # Make pokemon more angry
    elif request.POST['action'] == 'pokeball':
        request.session['pokeballs'] -= 1
        # random chance to catch pokemon
    elif request.POST['action'] == 'run':
        # Need to figure out how to return redirect back to /findPokemon/grass etc since it was passed through POST actions
        return HttpResponseRedirect('/findPokemon')
