from acc.models import User
from django.db import models

# Create your models here.

class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    likey = models.IntegerField()
    up = models.ManyToManyField(User)

    def __str__(self):
        return self.subject

class Reply(models.Model):
    subject = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=100)
    comment = models.TextField()
    pic = models.ImageField()
