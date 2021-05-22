from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class proFile(models.Model):
    usr= models.ForeignKey(User,on_delete=models.CASCADE)
    usrname= models.CharField(max_length=200)
    Bio= models.CharField(max_length=150,default=None,null=True)
    
    def __str__(self):
        return self.usr.username