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
    # username = forms.CharField()
    # password = forms.CharField(
    #     widget = forms.PasswordInput(
    #         attrs={
    #             "id":"password"
    #         }
    #     )
    # )

    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    ##################
    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid user.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid user.")
        return username
    # def validUser(user):
    #     username = user.cleaned_data.get("username")
    #     qs = User.objects.filted(username__iexact = username)
    #     if not qs.exists():
    #         raise forms.ValidationError("Invalid user, username does not exist")
    #     return username
