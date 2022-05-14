from django.shortcuts import render

from mysite.Blog.models import Blog

# Create your views here.

def home(request) :
    blogs = Blog.objects
    return render(request, 'home.html')

def new(request):
    return render(request, 'new.html')
