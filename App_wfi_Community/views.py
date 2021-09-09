from django.db.models.query_utils import Q
from App_wfi_Community import signals, urls
from django.shortcuts import render
from django.http import request, HttpResponseRedirect, HttpResponse
# import the models
from .models import Question, Answer, Comment, Upvote, DownVote, Upvote_record
# import paginator for pagination
from django.core.paginator import Paginator
# import forms
from .forms import Write_Answer_form, CommentForm
# import user
from django.contrib.auth.models import User
# import timezone for update function
from django.utils import timezone
# reverse for efficient url redirecting
from django.urls import reverse
from django.shortcuts import redirect
# import helper functions
from App_wfi_Community.view_helpers import *
# custom middleware
from App_wfi_Community.decorators import authentication_required, welcome_user_auth

# Create your views here.

# functions to called in views


def getPageObject(request, all_qns):
    """Returns the page object of Questions"""
    paginator = Paginator(all_qns, 4, orphans=3)
    pageNo = request.GET.get('page')


def getTags(RequestedQuestion):
    """Returns the Tags with comma seprated(if available)"""
    # get tags from Question model
    Question_tags = RequestedQuestion.Tags
    # check if tag are not empty
    if Question_tags != None:
        Tags = Question_tags.split(',')
    else:
        Tags = Question_tags
    # return the tags
    return Tags


def get_save_form_data(RequestedQuestion, request, fom):
    """get data from form & save to DB"""
    related_question = RequestedQuestion
    detail = fom.cleaned_data['detail']
    ansGiver = User.objects.get(pk=request.user.id)
    ans = Answer(AnsGiver=ansGiver,
                 related_question=related_question, detail=detail)
    ans.save()


# functions to process and send data to templates
@welcome_user_auth
def index(request):
    # check if user is typing something
    all_qns = Question.objects.all().order_by('-id')
    # passing all questions to paginator with 4 question for one page
    paginator = Paginator(all_qns, 6, orphans=2)
    # get page no from home.html element with name= 'page'
    page_number = request.GET.get('page')
    # making page object
    page = paginator.get_page(page_number) #this will be changed
    # get all answer objects
    all_ans = Answer.objects.all()
    # get the username to display on home
    username = request.user.username
    # pass all the data to dictionary
    data = {'all_ans': all_ans, 'all_qns': all_qns,
            'page_object': page, 'username': username}
    return render(request, 'home.html', data)


@authentication_required
def detail(request, questionID):
    # get the Question from ID
    RequestedQuestion = Question.objects.get(id=questionID)
    # get the tags
    Tags = getTags(RequestedQuestion)
    # get the Answer
    ans_A = Answer.objects.filter(related_question=RequestedQuestion)
    # get the comment form
    commentform = CommentForm()
    # pass the info to data
    data = {
        'RequestedQuestion': RequestedQuestion,
        'ans_A': ans_A,
        'Tags': Tags,
        'commentForm': commentform,
    }
    return render(request, 'detail.html', data)


@authentication_required
def writeAns(request, questionID):
    # get the Question from ID
    RequestedQuestion = Question.objects.get(id=questionID)
    # check if there is a post request from template
    if request.method == 'POST':
        # get all the form data with post request into a variable
        fom = Write_Answer_form(request.POST)
        if fom.is_valid():
            get_save_form_data(RequestedQuestion, request, fom)
            # make a string url to pass as a arguments
            url = '/detail/' + str(questionID)
            return HttpResponseRedirect(url)
        else:
            return HttpResponse('you write the answer incorrectly')
    else:
        # send blank form to template
        fom = Write_Answer_form()
        data = {'form': fom}
        return render(request, 'writeAns.html', data)


@authentication_required
def saveComment(request, ansID, questionID):
    if request.method == 'POST':
        fom = CommentForm(request.POST)
        if fom.is_valid():
            answer = Answer.objects.get(id=ansID)
            commented_By = User.objects.get(pk=request.user.id)
            detail = fom.cleaned_data['detail']
            comment = Comment(
                answer=answer, commented_By=commented_By, detail=detail)
            comment.save()
            # redirect the user to previous page
            url = '/detail/' + str(questionID)
            return HttpResponseRedirect(url)

# update the Answer


@authentication_required
def update(request, ansID):
    if request.method == 'POST':
        fom = Write_Answer_form(request.POST)
        if fom.is_valid():
            answer = Answer.objects.filter(id=ansID)
            # getting data for saving
            ansGiver = User.objects.get(pk=request.user.id)
            related_question = answer[0].related_question
            detail = '[Edited] ' + fom.cleaned_data['detail']
            post_time = timezone.now()
            # saving to database (for update we need to add all fields including answer id and post time)
            ansObj = Answer(id=ansID, AnsGiver=ansGiver,
                            related_question=related_question, detail=detail, post_time=post_time)
            ansObj.save()
            # getting question id for redirecting the url
            question = Question.objects.get(title=related_question)
            url = '/detail/' + str(question.id)
            return HttpResponseRedirect(url)
    else:
        fom = Write_Answer_form()
        data = {'form': fom}
        return render(request, 'update.html', data)

# delete the answer


@authentication_required
def deleteAns(request, ansID):
    answerOb = Answer.objects.get(id=ansID)
    question = Question.objects.get(title=answerOb.related_question)
    answerOb.delete()
    # url for redirection
    url = '/detail/'+str(question.id)
    return HttpResponseRedirect(url)


# search function
@authentication_required
def search(request):
    # usr_qry= request.GET['searchfieldText']
    # print(usr_qry)
    # for use with postgre
    # search_res1= Question.objects.filter(detail__icontains=usr_qry).order_by('id')
    # search_res2= Question.objects.filter(title__icontains=usr_qry).order_by('id')
    # final_res= search_res1.union(search_res2)
    # final_res= Question.objects.filter(Q(title__icontains=usr_qry) or Q(detail__icontains=usr_qry))
    # print('the search res are:',final_res)
    # pag_ob= Paginator(final_res,per_page=3)
    # print(f"Total no of question found with search are: {pag_ob.count}")
    # print(f"Total no of pages found with the question are: {pag_ob.num_pages}")
    # print(f"The Page range is: {pag_ob.page_range}")
    # print('the item in the page 1 are:',pag_ob.page(1).object_list)
    return HttpResponse('search functionality is not available yet')


def downVote(request, ansID, quesID):
    url= "/detail/"+str(quesID)
    usr= User.objects.get(pk= request.user.id)
    ansob= Answer.objects.get(id=ansID)
    if chk_downvote_record(usr,ansob) == "yes":
        print('this ans is already downvoted by: ',usr)
    elif chk_downvote_record(usr,ansob) == "no":
        save_to_downvote_record(usr,ansob)
        update_downvote(ansob)
        signals.delete_upVote.send(sender=None,ans=ansob,usr=usr)
    return HttpResponseRedirect(url)



def upvote(request, ansID, quesID):
    url = "/detail/"+str(quesID)
    usr = User.objects.get(pk=request.user.id)
    ans_ob = Answer.objects.get(id=ansID)
    if check_upvote_record(usr, ans_ob) == "yes":
        pass
    elif check_upvote_record(usr, ans_ob) == "no":
        save_to_upvt_rec(usr, ans_ob)
        update_upvote(ans_ob)
        signals.delete_downvote.send(sender=None,ans=ans_ob,usr=usr)
    return HttpResponseRedirect(url)