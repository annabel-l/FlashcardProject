from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def homeScreen(request):

    cardSets = CardSet.objects.all()
    #filter for only can see your own sets when logged in later
    list = {}
    for set in cardSets:
        list[set.name] = set.id
        print(set.id)
    
    
    return render(request, 'home.html', {"cardSets": list})

def cardScreen(request):

   #setId = request.POST['setId']
    #cards = Card.objects.get(id=setId)
    cards = Card.objects.all()
    #filter for only can see your own sets when logged in later
    #filter depending on what button is clicked
    list = {}
    for card in cards:
        list[card.front] = [card.back, card.id]
        print( "stuff: " + card.back)
        print(card.id)
    
    
    return render(request, 'cards.html', {"cards": list})
    
    
