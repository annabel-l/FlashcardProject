from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class CardSet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,null = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    importance = models.BooleanField(default = False, null = True)
    tag = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.name


class Card(models.Model):
    front = models.CharField(max_length=1000, null = True)
    back = models.CharField(max_length=1000, null = True)
    set = models.ForeignKey(CardSet,null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.front
    




