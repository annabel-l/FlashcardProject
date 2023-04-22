from django.urls import path
from django.views.generic import TemplateView

from cards.views import *

urlpatterns = [
    path(
        "", homeScreen , name="homeScreen"
    ),
    path("/cards",  cardScreen, name = "cardView"),
]