from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image, Comment, Profile
from .forms import NewImageForm, SignupForm

from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            profile = Profile(user=user)
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Instagram account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required(login_url='/accounts/login/')
def all_images(request):
    date = dt.date.today()
    images = Image.get_all()
    comments = Comment.get_comments()
    return render(request, 'index.html', {"date": date, "images": images, "comments": comments})


@login_required(login_url='/accounts/login/')
def my_profile(request, profile_id):
    date = dt.date.today()
    profile = Profile.objects.filter(id=profile_id)
    images = Image.objects.filter(user=request.user)
    return render(request, 'profile.html', {"date": date, "profile": profile, "images": images, })


def explore(request):
    date = dt.date.today()
    profiles = Profile.get_profiles()
    return render(request, 'explore.html', {"date": date, "profiles": profiles})


@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('all_images')
    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form": form})
