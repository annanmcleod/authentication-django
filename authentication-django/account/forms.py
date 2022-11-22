from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        # widgets = {
        #     "username": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Username"}
        #     ),
        #     "email": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Email"}
        #     ),
        #     "password1": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Password"}
        #     ),
        #     "password2": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Confirm Password"}
        #     ),
        # }


class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "birthdate", "gender"]
        # fields = "__all__"
        # # fields = ["name", "birthdate", "gender"]

        # widgets = {
        #     "name": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Name"}
        #     ),
        #     "birthdate": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Birthdate"}
        #     ),
        #     "gender": forms.TextInput(
        #         attrs={"class": "form-control", "placeholder": "Gender"}
        #     ),
        # }
