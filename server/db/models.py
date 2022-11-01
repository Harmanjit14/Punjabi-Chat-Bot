from uuid import uuid4
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):

    id = models.UUIDField(default=uuid4,primary_key=True,editable=False)
    name = models.CharField(max_length=255,blank=False)
    dob = models.DateField()
    father_name =models.CharField(max_length=255,blank=False)
    mother_name = models.CharField(max_length=255,blank=False)
    song_choice = models.CharField(max_length=255,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.name
    
