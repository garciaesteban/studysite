from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = "study"

urlpatterns = [
    path("", RedirectView.as_view(url="home")),
    path("home/", views.home, name="home"),
    path("createuser", views.createuser, name="createuser"),
    path("loginuser", views.loginuser, name="loginuser"),
    path("logout", views.logoutuser, name="logoutuser"),
    path("createnote/<int:bookid>", views.createnote, name="createnote"),
    path("delete/book/<int:book>", views.deletebook, name="deletebook"),
    path("delete/note/<int:note>", views.deletenote, name="deletenote"),
    path("details/<int:book>", views.bookdetail, name="detailbook"),
    path("edit/note/<int:noteid>", views.editnote, name="editnote"),
    path("edit/book/<int:bookid>", views.editbook, name="editbook"),
]
