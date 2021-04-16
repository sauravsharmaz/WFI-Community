from App_wfi_Community.models import Question
from django import forms
from django.core import validators

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model= Question
        fields= ['title','detail','Tags']


