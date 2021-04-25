from django.shortcuts import render
from django.http import request,HttpResponseRedirect, HttpResponse
from App_wfi_Community.models import Question 
from askQuestion.forms import AskQuestionForm
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def ask(request):
    if request.method == 'POST':
        fom= AskQuestionForm(request.POST)
        if fom.is_valid():
            AskedBy= User.objects.get(pk=request.user.id)
            title= fom.cleaned_data['title']
            detail= fom.cleaned_data['detail']
            ask_time= timezone.now()
            Tags= fom.cleaned_data['Tags']
            questOb= Question(AskedBy=AskedBy,title=title,detail= detail,ask_time=ask_time,Tags=Tags)
            questOb.save()
            # redirect the user to home
            return HttpResponseRedirect(reverse('success_page'))
    else:
        fom= AskQuestionForm()
        data= {'form':fom}
        return render(request, 'askQuestion/index.html',data)

def success(request):
    return render(request, 'askQuestion/redirect.html')