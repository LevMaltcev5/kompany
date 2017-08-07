from django import forms
from .models import *

class RegMailClient(forms.ModelForm):

    class Meta:
        model = MyClient
        exclude = ["day","time","phone"]

class RegPhoneClient(forms.ModelForm):

    class Meta:
        model = MyClient
        exclude = ["email"]
