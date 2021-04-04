from django.db import models

# importing user
from django.contrib.auth.models import User


class Question(models.Model):
    """(User Question Model)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    detail = models.TextField()
    ask_time = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.title


class Answer(models.Model):
    """(User Answer Model)"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    detail = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return self.detail
