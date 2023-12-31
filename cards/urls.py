from django.urls import path
from django.views.generic import TemplateView

from cards.views import *

urlpatterns = [
    path(
        "", homeScreen , name="homeScreen"
    ),
    path(
        "/homescreen", homeScreen , name="homeScreen"
    ),
    path("/cards",  cardScreen, name = "cardView"),
    path("/deleteSet",  deleteSet, name = "deleteSet"),
    path("/addSet",  addSet, name = "addSet"),
    path("/deleteCard",  deleteCard, name = "deleteCard"),
    path("/addCard",  addCard, name = "addCard"),
    path('star/', markImportant, name = "important"),
    path("login/",  loginCheck, name = "login"),
    path('logout/', logoutCheck, name = "logout"),
    path('register/', registerCheck, name = "register"),
    path("/search", searchResults, name="search"),
    path("/azSort", azSorting, name = "azSort"),
    path("/newSort", newSorting, name = "newSort"),
    path("/oldSort", oldSorting, name = "oldSort"),
    path("/impSort", impSorting, name = "impSort")
]