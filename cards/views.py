from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from accounts.views import *
from django.db.models import Q


def homeScreen(request):

    
   
    
    sort = request.session.get('sort')
    #checking sort display method
    if sort == "imp":
        return impSorting(request)
    elif sort == "az":
        return azSorting(request)
    elif sort == "new":
        return newSorting(request)
    elif sort == "old":
        return oldSorting(request)

    try:
        userId = request.session.get('userId')
        user = User.objects.get(id = userId)
        cardSets = CardSet.objects.filter(owner = user)
        list = {}
        for set in cardSets:
            list[set.name] = [set.id, set.tag, set.importance]
            
        
        return render(request, 'home.html', {"cardSets": list})
    except:
         return render(request, 'home.html')

    

def cardScreen(request):

    setId = request.POST['setId']
    cardSet = CardSet.objects.get(id=setId)
    cards = Card.objects.filter(set = cardSet)
   
    list = {}
    request.session['setId'] = setId
    for card in cards:
        list[card.front] = [card.back, card.id]
        print( "stuff: " + card.back)
        print(card.id)
    
    
    return render(request, 'cards.html', {"cards": list, "tag":cardSet.tag, "name":cardSet.name})

def deleteSet(request):
    try:
        setId = request.POST['setId']
        cardSet = CardSet.objects.get(id=setId)
        cards = Card.objects.filter(set = cardSet).delete()
        cardSet.delete()
    except:
        pass
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
    try:
        cardId = request.POST['item']
        Card.objects.get(id=cardId).delete()
    except:
        pass

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

def searchResults(request):
    userId = request.session.get('userId')
    user = User.objects.get(id = userId)
    query = request.GET.get("search")
    cardSets = CardSet.objects.filter(owner = user)
    results = cardSets.filter(Q(name__icontains=query)|Q(tag__icontains=query))

    resultList = {}
    for set in results:
        resultList[set.name] = [set.id]

    return render(request, 'search.html', {"results":resultList})

def azSorting(request):
    request.session['sort'] = "az"
    userId = request.session.get('userId')
    user = User.objects.get(id = userId)
    azSets = CardSet.objects.order_by('name')
    cardSets = azSets.filter(owner = user)
    list = {}
    for set in cardSets:
        list[set.name] = [set.id, set.importance]
    return render(request, 'home.html', {"cardSets": list, "sort": "alphabetically"})

def newSorting(request):
    request.session['sort'] = "new"
    userId = request.session.get('userId')
    user = User.objects.get(id = userId)
    dateSets = CardSet.objects.order_by('-date_created')
    cardSets = dateSets.filter(owner = user)
    list = {}
    for set in cardSets:
        list[set.name] = [set.id, set.importance]
    return render(request, 'home.html', {"cardSets": list, "sort": "by your newest sets"})

def oldSorting(request):
    request.session['sort'] = "old"
    userId = request.session.get('userId')
    user = User.objects.get(id = userId)
    dateSets = CardSet.objects.order_by('date_created')
    cardSets = dateSets.filter(owner = user)
    list = {}
    for set in cardSets:
        list[set.name] = [set.id, set.importance]
    return render(request, 'home.html', {"cardSets": list, "sort": "your oldest sets"})

def impSorting(request):
    request.session['sort'] = "imp"
    userId = request.session.get('userId')
    user = User.objects.get(id = userId)
    impSets = CardSet.objects.order_by('-importance')
    cardSets = impSets.filter(owner = user)
    list = {}
    for set in cardSets:
        list[set.name] = [set.id, set.importance]
    return render(request, 'home.html', {"cardSets": list, "sort": "by importance"})

# def sortHomeScreen(request):

    
#     #filter for only can see your own sets when logged in later
#     try:
#         userId = request.session.get('userId')
#         user = User.objects.get(id = userId)
#         cardSets = CardSet.objects.filter(owner = user)
#         list = {}
#         for set in cardSets:
#             list[set.name] = [set.id, set.tag, set.importance]
            
        
#         return render(request, 'home.html', {"cardSets": list})
#     except:
#          return render(request, 'home.html')