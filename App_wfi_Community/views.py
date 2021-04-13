from django.shortcuts import render
from django.shortcuts import render
from django.http import request, HttpResponseRedirect, HttpResponse
# import the models 
from .models import Question, Answer, Comment
# import paginator for pagination
from django.core.paginator import Paginator
# import forms
from .forms import Write_Answer_form, CommentForm
# import user
from django.contrib.auth.models import User

# Create your views here.

# functions to called in views 

def getTags(RequestedQuestion):
  # get tags from Question model
  Question_tags= RequestedQuestion.Tags
  # check if tag are not empty
  if Question_tags != None:
    Tags= Question_tags.split(',')
  else:
    Tags= Question_tags
  # return the tags
  return Tags

def get_save_form_data(RequestedQuestion, request, fom):
  """get data from form & save to DB"""
  related_question= RequestedQuestion
  detail= fom.cleaned_data['detail']
  ansGiver= User.objects.get(pk= request.user.id)
  ans= Answer(AnsGiver= ansGiver,related_question= related_question,detail=detail)
  ans.save()

def search(request):
  if 'searchfieldText' in request.GET:
    usrQuery= request.GET['searchfieldText']
    # search the usrQuery
    searchRes= Question.objects.filter(title__icontains= usrQuery)
    # sort the result by latest
    all_qns= searchRes.order_by('-id')
    return all_qns
  else:
    # get all objects of question model with latest as first
    all_qns= Question.objects.all().order_by('-id')
    return all_qns


# functions to process and send data to templates

def index(request):
  # check if user is typing something
  all_qns= search(request)  
  # passing all questions to paginator with 4 question for one page
  paginator= Paginator(all_qns, 4, orphans=2)
  # get page no from home.html element with name= 'page'
  page_number= request.GET.get('page')
  # making page object
  page_object= paginator.get_page(page_number)
  # get all answer objects
  all_ans= Answer.objects.all()
  # pass all the data to dictionary
  data={'all_ans':all_ans,'all_qns':all_qns,'page_object':page_object}
  return render(request,'home.html', data) 

 
def detail(request,questionID):
  # get the Question from ID
  RequestedQuestion= Question.objects.get(id= questionID)
  # get the tags
  Tags= getTags(RequestedQuestion)
  # get the Answer
  ans_A= Answer.objects.filter(related_question= RequestedQuestion)
  # get the comment form
  commentform= CommentForm()
  # pass the info to data 
  data= {
    'RequestedQuestion':RequestedQuestion,
    'ans_A':ans_A,
    'Tags':Tags,
    'commentForm':commentform,
    }
  return render(request, 'detail.html', data)




def writeAns(request,questionID):
  # get the Question from ID
  RequestedQuestion= Question.objects.get(id= questionID)
  # check if there is a post request from template
  if request.method == 'POST':
    # get all the form data with post request into a variable
    fom= Write_Answer_form(request.POST)
    if fom.is_valid():
      get_save_form_data(RequestedQuestion, request, fom)
      # make a string url to pass as a arguments
      url= '/detail/'+ str(questionID)
      return HttpResponseRedirect(url)
  else:
    # send blank form to template
    fom= Write_Answer_form()
    data= {'form':fom}
    return render(request, 'writeAns.html', data)

def saveComment(request, ansID, questionID):  
  if request.method == 'POST':
    fom= CommentForm(request.POST)
    if fom.is_valid():
      answer= Answer.objects.get(id=ansID)
      commented_By= User.objects.get(pk= request.user.id)
      detail= fom.cleaned_data['detail']
      comment= Comment(answer=answer,commented_By=commented_By,detail=detail)
      comment.save()
      # redirect the user to previous page
      url= '/detail/'+ str(questionID)
      return HttpResponseRedirect(url)



