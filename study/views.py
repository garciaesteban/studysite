from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm, BookForm, NoteForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django import forms
from django.forms import Select
import datetime

# Create your views here.


def editbook(request, bookid):
    template = "study/editbook/editbook.html"
    book = Book.objects.get(id=bookid)
    context = {}
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book.title = form.cleaned_data["title"]
            book.author = form.cleaned_data["author"]
            book.publisher = form.cleaned_data["publisher"]
            if form.cleaned_data["finished_reading"] == True:
                book.finished_reading = datetime.date.today()
            elif (
                book.finished_reading is not None
                and form.cleaned_data["finished_reading"] == False
            ):
                book.finished_reading = None
            book.save()
            return redirect(request.POST["next"])
        else:
            context["bookForm"] = form
            context["book"] = bookid
            context["back"] = request.POST["next"]
            context["next"] = request.POST["next"]
    else:
        context["bookForm"] = BookForm(
            {
                "title": book.title,
                "author": book.author,
                "publisher": book.publisher,
                "finished_reading": book.finished_reading,
                "chapters": book.chapters,
            }
        )
        context["book"] = bookid
        context["back"] = request.META["HTTP_REFERER"]
        context["next"] = request.META["HTTP_REFERER"]

    return render(request, template, context)


def editnote(request, noteid):
    template = "study/editnote/editnote.html"
    n = Note.objects.get(id=noteid)
    context = {}
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            n.title = form.cleaned_data["title"]
            n.text = form.cleaned_data["text"]
            n.chapter = form.cleaned_data["chapter"]
            n.start_page = form.cleaned_data["start_page"]
            n.end_page = form.cleaned_data["end_page"]
            n.save()
            return redirect(request.POST["next"])
        else:
            context["noteForm"] = form
            context["note_id"] = noteid
            context["back"] = request.POST["next"]
            context["next"] = request.POST["next"]
    else:
        context["noteForm"] = NoteForm(
            {
                "title": n.title,
                "text": n.text,
                "chapter": n.chapter,
                "start_page": n.start_page,
                "end_page": n.end_page,
            }
        )
        context["note_id"] = noteid
        context["back"] = request.META["HTTP_REFERER"]
        context["next"] = request.META["HTTP_REFERER"]

    return render(request, template, context)


def deletenote(request, note):
    n = Note.objects.get(id=note)
    n.delete()
    return redirect(request.META["HTTP_REFERER"])


def deletebook(request, book):
    b = Book.objects.get(id=book)
    b.delete()
    return redirect("study:home")


def bookdetail(request, book):
    template = "study/bookdetail/bookdetail.html"
    book = Book.objects.get(id=book)
    notes = Note.objects.filter(book=book).order_by("-date_created", "-pk")
    context = {}
    context["book"] = book
    context["notes"] = notes
    return render(request, template, context)


def createnote(request, bookid):
    template = "study/createnote/createnote.html"
    context = {}
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            book = Book.objects.get(id=bookid)
            note = Note(
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"],
                chapter=form.cleaned_data["chapter"],
                start_page=form.cleaned_data["start_page"],
                end_page=form.cleaned_data["end_page"],
                book=book,
            )
            note.save()
            return redirect(request.POST["next"])
        else:
            context["noteForm"] = form
            context["bookid"] = bookid
            context["back"] = request.POST["next"]
            context["next"] = request.POST["next"]
    else:
        context["noteForm"] = NoteForm()
        context["bookid"] = bookid
        context["back"] = request.META["HTTP_REFERER"]
        context["next"] = request.META["HTTP_REFERER"]

    return render(request, template, context)


@login_required(login_url="study:loginuser")
def home(request):
    template = "study/home/user-home.html"
    context = {}
    listCombine = []
    books = Book.objects.filter(user=request.user).order_by("-started_reading", "-pk")

    for book in books:
        notes = Note.objects.filter(book=book).order_by("-date_created", "-pk")[:6]
        listCombine.append([book, notes])

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=request.user)
            n = Book(
                title=form.cleaned_data["title"],
                author=form.cleaned_data["author"],
                publisher=form.cleaned_data["publisher"],
                chapters=form.cleaned_data["chapters"],
                user=user,
            )
            n.save()
            return redirect("study:home")
        else:
            context["errorBookForm"] = form
            context["bookForm"] = BookForm()
    else:
        user = User.objects.get(username=request.user)
        context["bookForm"] = BookForm()

    context["listCombine"] = listCombine
    return render(request, template, context)


def createuser(request):
    template = "study/auth/createuser.html"
    context = {}
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("study:home")
        else:
            context["form"] = form
    else:
        form = CustomUserCreationForm()
        context["form"] = form
    return render(request, template, context)


def loginuser(request):
    template = "study/auth/loginuser.html"
    context = {}
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("study:home")
            else:
                context["form"] = form
        else:
            context["form"] = form
    else:
        form = CustomAuthenticationForm()
        context["form"] = form
    return render(request, template, context)


def logoutuser(request):
    logout(request)
    return redirect("study:loginuser")
