from django.shortcuts import render
from django.shortcuts import render
from django.http import request
# import the models
from .models import Question, Answer
# import paginator for pagination
from django.core.paginator import Paginator

# Create your views here.

def index(request):
  request.session.flush()
  # check if user is typing something
  if 'searchfieldText' in request.GET:
    usrQuery= request.GET['searchfieldText']
    # search the usrQuery
    searchRes= Question.objects.filter(title__icontains= usrQuery)
    # sort the result by latest
    all_qns= searchRes.order_by('-id')
  else:
    # get all objects of question model with latest as first
    all_qns= Question.objects.all().order_by('-id')
  
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
  request.session.flush()
  RequestedQuestion= Question.objects.get(id= questionID)
  ansOfRequestedQtn= Answer.objects.filter(related_question= RequestedQuestion)
  data= {'RequestedQuestion':RequestedQuestion,'ansOfRequestedQtn':ansOfRequestedQtn}
  return render(request, 'detail.html', data)