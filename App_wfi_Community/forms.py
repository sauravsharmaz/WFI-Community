from django.core import validators
from django import forms
from .models import *

class AddAns(forms.ModelForm):
	class Meta:
		model= Answer
		fields= ['related_question','detail','AnsGiver']


class Write_Answer_form(forms.ModelForm):
	class Meta:
		model= Answer
		fields= ['detail']

