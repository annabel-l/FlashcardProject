from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from accounts.views import *


def homeScreen(request):

    
    #filter for only can see your own sets when logged in later
    try:
        userId = request.session.get('userId')
        user = User.objects.get(id = userId)
        cardSets = CardSet.objects.filter(owner = user)
        list = {}
        for set in cardSets:
            list[set.name] = [set.id, set.importance]
            
        
        return render(request, 'home.html', {"cardSets": list})
    except:
         return render(request, 'home.html')
    

def cardScreen(request):

    setId = request.POST['setId']
    cardSet = CardSet.objects.get(id=setId)
    cards = Card.objects.filter(set = cardSet)
    #filter for only can see your own sets when logged in later
    #filter depending on what button is clicked
    list = {}
    request.session['setId'] = setId
    for card in cards:
        list[card.front] = [card.back, card.id]
        print( "stuff: " + card.back)
        print(card.id)
    
    
    return render(request, 'cards.html', {"cards": list})

def deleteSet(request):
    setId = request.POST['setId']
    cardSet = CardSet.objects.get(id=setId)
    cards = Card.objects.filter(set = cardSet).delete()
    cardSet.delete()
    return homeScreen(request)


def addSet(request):

    setName = request.POST['name']
    setTag = request.POST['tag']
    userId = request.session.get('userId')
    user = User.objects.get( id = userId)
   
    cardSet = CardSet(owner = user, name = setName, tag = setTag)
    cardSet.save()
    return homeScreen(request)


    
    #return homeScreen(request)

def deleteCard(request):

    cardId = request.POST['item']

    Card.objects.get(id=cardId).delete()
    return updateCardScreen(request)

def addCard(request):
    
    front = request.POST['front']
    back = request.POST['back']
    setId = request.session.get('setId')
    set = CardSet.objects.get(id = setId)
    newCard = Card(front = front, back = back, set = set)
    newCard.save()

    return updateCardScreen(request)


    
    #return homeScreen(request)
   
def updateCardScreen(request):
    setId = request.session.get('setId')
    cardSet = CardSet.objects.get(id=setId)
    cards = Card.objects.filter(set = cardSet)
    #filter for only can see your own sets when logged in later
    #filter depending on what button is clicked
    list = {}
    for card in cards:
        list[card.front] = [card.back, card.id]
        print( "stuff: " + card.back)
        print(card.id)
    return render(request, 'cards.html', {"cards": list})

def markImportant(request):
    setId = request.POST['setId']
    cardSet = CardSet.objects.get(id=setId)
    if cardSet.importance:
        cardSet.importance = False
    else:
        cardSet.importance = True
    cardSet.save()
    return homeScreen(request)

    