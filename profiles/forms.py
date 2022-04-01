
from operator import imod
from socket import fromshare
from django import forms
from .models import *

class ProfilePicForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['profile_pic']
