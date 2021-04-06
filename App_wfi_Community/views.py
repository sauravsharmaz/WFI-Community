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
  # get all objects of question model
  all_qns= Question.objects.all().order_by('id')
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


def ans(request,idl):
  request.session.flush()
  print("the slig param is ====>",idl)
  # all_ans= Answer.objects.all()
  # mainAns= Answer.objects.get(related_question__title= qtn_title)
  # print("the filter is working and the value is=====>",mainAns)
  # mainAn= Answer.objects.filter(related_question__title= "what is django.?")
  # print("the answer is ===> ", mainAn)
  return render(request, 'answers.html')