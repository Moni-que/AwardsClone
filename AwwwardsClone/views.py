from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Review
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
@login_required(login_url = "signin")
def index(request):
    return render(request, 'all_templates/index.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #login user and redirect to settings page
                user_login = auth.authenticate(username=username, password=password)
                # auth.login(request, user_login)
                return redirect('signin')

        else:
            messages.info(request, 'Passwords must match')
            return redirect('signup')

    else:
        return render(request, 'all_templates/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')

    return render(request, 'all_templates/signin.html')

