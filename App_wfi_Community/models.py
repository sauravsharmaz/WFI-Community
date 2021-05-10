from django.db import models
# importing user
from django.contrib.auth.models import User
from django.utils import timezone

# we used foreign key for many to one relationship
class Question(models.Model):
    """(User Question Model)"""
    id= models.AutoField(primary_key= True)
    AskedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    detail = models.TextField()
    ask_time = models.DateTimeField(auto_now_add=True)
    Tags= models.TextField(null=True)
    def __str__(self):
        return self.title

class Answer(models.Model):
    """(User Answer Model)"""
    id= models.AutoField(primary_key= True)
    AnsGiver= models.ForeignKey(User, on_delete= models.CASCADE)
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.detail

class Comment(models.Model):
    """(User Comment Model)"""
    id= models.AutoField(primary_key= True)
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)
    commented_By= models.ForeignKey(User, on_delete= models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)
    detail= models.TextField(null=True)
    def __str__(self):
        return self.detail

class Upvote(models.Model):
    """(User Upvote Model)"""
    id= models.AutoField(primary_key= True)
    value= models.BigIntegerField(default=0,null=True)
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)

    def __str__(self):
        return str(self.value)
    
class Upvote_record(models.Model):
    """Contains all upvote record for every user"""
    id= models.AutoField(primary_key=True)
    val= models.IntegerField(null=True,default=None)
    ans= models.ForeignKey(Answer,on_delete=models.CASCADE)
    usr= models.ForeignKey(User,on_delete=models.CASCADE,default=None,null=True)

class DownVote(models.Model):
    """(User DownVote Model)"""
    id= models.AutoField(primary_key= True)
    value= models.BigIntegerField(default=0,null=True)
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)
    DownVote_By= models.ForeignKey(User, on_delete= models.CASCADE)

