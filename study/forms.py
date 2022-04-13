from django import forms
from django.forms import (
    ModelForm,
    TextInput,
    PasswordInput,
    EmailInput,
    CheckboxInput,
    Textarea,
    NumberInput,
    Select,
    DateInput,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Book


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        max_length=150,
        widget=PasswordInput(attrs={"class": "form-control"}),
        label="Password",
    )
    password2 = forms.CharField(
        max_length=150,
        widget=PasswordInput(attrs={"class": "form-control"}),
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        widgets = {
            "username": TextInput(attrs={"class": "form-control shadow-none"}),
            "first_name": TextInput(attrs={"class": "form-control shadow-none"}),
            "last_name": TextInput(attrs={"class": "form-control shadow-none"}),
            "email": EmailInput(attrs={"class": "form-control shadow-none"}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=150, widget=TextInput(attrs={"class": "form-control shadow-none"})
    )
    password = forms.CharField(
        max_length=150,
        widget=PasswordInput(attrs={"class": "form-control shadow-none"}),
    )


class BookForm(forms.Form):
    title = forms.CharField(
        max_length=255, widget=TextInput(attrs={"class": "form-control shadow-none"})
    )
    author = forms.CharField(
        max_length=255,
        required=False,
        widget=TextInput(attrs={"class": "form-control shadow-none"}),
    )
    publisher = forms.CharField(
        max_length=255,
        required=False,
        widget=TextInput(attrs={"class": "form-control shadow-none"}),
    )
    chapters = forms.IntegerField(widget=NumberInput(attrs={"class": "form-control"}))
    finished_reading = forms.BooleanField(
        required=False,
        widget=CheckboxInput(attrs={"class": "form-check-input", "type": "checkbox"}),
    )


class NoteForm(forms.Form):
    title = forms.CharField(
        max_length=255, widget=TextInput(attrs={"class": "form-control shadow-none"})
    )
    text = forms.CharField(widget=Textarea(attrs={"class": "form-control shadow-none"}))
    chapter = forms.IntegerField(
        widget=NumberInput(attrs={"class": "form-control shadow-none"})
    )
    start_page = forms.IntegerField(
        widget=NumberInput(attrs={"class": "form-control shadow-none"})
    )
    end_page = forms.IntegerField(
        widget=NumberInput(attrs={"class": "form-control shadow-none"})
    )
