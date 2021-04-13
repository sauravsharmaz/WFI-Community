from django.core import validators
from django import forms
from .models import *

class CommentForm(forms.ModelForm):
	class Meta:
		model= Comment
		fields= ['detail']


class Write_Answer_form(forms.ModelForm):
	class Meta:
		model= Answer
		fields= ['detail']

