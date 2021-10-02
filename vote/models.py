from django.db import models
from acc.models import User
# Create your models here.
class Voter(models.Model):
    subject = models.CharField(max_length=30)
    wrtier = models.CharField(max_length=30)
    comment = models.TextField()
    voter = models.ManyToManyField(User)
    
    def __str__(self):
        return self.subject

class Vote(models.Model):
    subject = models.ForeignKey(Voter, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    num = models.IntegerField(default=0)
    # image = models.ImageField(upload_to=f"vote/{subject}")

    def __str__(self):
        return self.name    


