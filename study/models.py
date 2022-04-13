from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    chapter = models.PositiveIntegerField()
    start_page = models.PositiveIntegerField()
    end_page = models.PositiveIntegerField()
    date_created = models.DateField(auto_now_add=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    started_reading = models.DateField(auto_now_add=True)
    finished_reading = models.DateField(blank=True, null=True)
    chapters = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
