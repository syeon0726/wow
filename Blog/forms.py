from django import forms
from .models import Page

class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = ['title', 'content', 'score']
        title = forms.CharField(max_length= 50)
        content = forms.CharField()
        score = forms.IntegerField()