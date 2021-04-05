from django.shortcuts import render
from django.shortcuts import render
from django.http import request
from .models import Question, Answer

# Create your views here.

def index(request):
  all_qns= Question.objects.all()
  all_ans= Answer.objects.all()
  qt_title= request.GET.get('question_title','no item')
  print('form el ===>',qt_title)
  data={'all_ans':all_ans,'all_qns':all_qns}
  return render(request,'home.html', data) 


def ans(request,qtn_title):
  # all_ans= Answer.objects.all()
  # mainAns= Answer.objects.get(related_question= qtn_title)
  # print(mainAns)
  return render(request, 'answers.html')