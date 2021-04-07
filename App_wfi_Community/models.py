from django.db import models

# importing user
from django.contrib.auth.models import User

class Question(models.Model):
    """(User Question Model)"""
    AskedBy = models.ForeignKey(User, on_delete=models.CASCADE, default="Anonymous User")
    title = models.CharField(max_length=500)
    detail = models.TextField()
    ask_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Answer(models.Model):
    """(User Answer Model)"""
    AnsGiver= models.ForeignKey(User, on_delete= models.CASCADE)
    related_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.detail

class Comment(models.Model):
    """(User Comment Model)"""
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)
    commented_By= models.ForeignKey(User, on_delete= models.CASCADE)
    post_time = models.DateTimeField(auto_now_add=True)

class Upvote(models.Model):
    """(User Upvote Model)"""
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)
    Upvote_By= models.ForeignKey(User, on_delete= models.CASCADE)

class DownVote(models.Model):
    """(User DownVote Model)"""
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)
    DownVote_By= models.ForeignKey(User, on_delete= models.CASCADE)