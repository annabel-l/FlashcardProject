from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput()
    )
    def uniqueUser(user):
        username = user.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact = username)
        if qs.exists():
            raise forms.ValidationError("Pick a different username")


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                "id":"password"
            }
        )
    )

    def validUser(user):
        username = user.cleaned_data.get("username")
        qs = User.objects.filted(username__iexact = username)
        if not qs.exists():
            raise forms.ValidationError("Invalid user, username does not exist")
        return username