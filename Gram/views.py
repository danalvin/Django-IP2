from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import datetime as dt
from .models import Image, Comment, Profile
from .forms import NewImageForm


# Create your views here.



def all_images(request):
    date = dt.date.today()
    images = Image.get_all()
    comments = Comment.get_comments()
    return render(request, 'index.html', {"date": date, "images": images, "comments": comments})


@login_required(login_url='/accounts/login/')
def my_profile(request,profile_id):
    date = dt.date.today()
    profiles = Profile.objects.filter(id = profile_id)
    images = Image.get_all()
    return render(request, 'profile.html', {"date": date, "profiles": profiles, "images": images, })

def explore(request):
    date = dt.date.today()
    profiles = Profile.get_profiles()
    return render(request, 'explore.html', {"date": date, "profiles": profiles})


def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form })

