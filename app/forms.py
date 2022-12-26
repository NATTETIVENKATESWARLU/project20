from django import forms
from app.models import *


class SchoolForm(forms.Form):
    name=forms.CharField(max_length=200)
    principal=forms.CharField(max_length=200)
    location=forms.CharField(max_length=200)
