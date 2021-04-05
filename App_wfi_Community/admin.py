from django.contrib import admin
from App_wfi_Community.models import Question, Answer, Comment, Upvote, DownVote

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display= ('title','AskedBy')
    search_fields= ('title', 'detail','ask_time','AskedBy__username')

class AnswerAdmin(admin.ModelAdmin):
    list_display= ('detail','related_question','AnsGiver')
    search_fields= ('detail','related_question__title','AnsGiver__username')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Comment)
admin.site.register(Upvote)
admin.site.register(DownVote)
