from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.username


class CardSet(models.Model):
    owner = models.ForeignKey(User,null = True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null = True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
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


