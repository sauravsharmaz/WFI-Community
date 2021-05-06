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
    Upvote_By= models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return str(self.value)
    

class DownVote(models.Model):
    """(User DownVote Model)"""
    id= models.AutoField(primary_key= True)
    value= models.BigIntegerField(default=0,null=True)
    answer= models.ForeignKey(Answer, on_delete= models.CASCADE)
    DownVote_By= models.ForeignKey(User, on_delete= models.CASCADE)


# def upvote(request, ansID):
#   ansOb= Answer.objects.get(id=ansID)
#   try:
#     upvote_Ob= Upvote.objects.get(answer=ansOb)
#     upvtID= upvote_Ob.id
#     value= (upvote_Ob.value)+1
#     Upvote_By= User.objects.get(pk= request.user.id)
#   except Exception as e:
#     print('exception in upvote: ',e)
#     value= 1
#     Upvote_By= User.objects.get(pk= request.user.id)
#     upvtOb= Upvote(value=value,answer=ansOb,Upvote_By=Upvote_By)
#     upvtOb.save()
#     print('but i maked a upvote obj for this question & saved it successfully.!')
#     return HttpResponse('You Upvoted this Question')

#   # saving the upvote to upvote model
#   try:
#     if Upvote.objects.filter(id=upvtID,Upvote_By=Upvote_By).count() == 0:
#       upvt= Upvote(id=upvtID,answer=ansOb,value=value,Upvote_By=Upvote_By)
#       upvt.save()
#       print('saved successfully.!')
#     else:
#       return HttpResponse('you cant upvote more than one time')
#   except Exception as e:
#     print('a exception has came: ')
#     print(e)
#   # print('saved successfully.!')
#   return HttpResponse('you upvoted the answer ')