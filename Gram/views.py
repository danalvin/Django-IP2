from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image, Comment, Profile
import datetime as dt



# Create your views here.
# def home(request):
#     return render(request, 'index.html')
#
def all_images(request):
    date = dt.date.today()
    images = Image.get_all()
    Comments = Comment.get_comments()

    return render(request, 'index.html',locals())
