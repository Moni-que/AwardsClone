from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project, Review
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import ProjectForm
# Create your views here.
@login_required(login_url = "signin")
def index(request):
    projects = Project.objects.all()
    return render(request, 'all_templates/index.html',{'projects':projects})

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
            return redirect('index')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('signin')

    return render(request, 'all_templates/signin.html')

@login_required(login_url = "signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url = "signin")
def upload(request):
    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.save()
            messages.success(request, "You have successfully posted your project!")
            return redirect('index')
    else:
        form=ProjectForm()
    return render(request,"all_templates/uploading_project.html",{'form':form}) 

@login_required(login_url = "signin")
def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term=request.GET.get('search')
        images=Project.search_results_name(search_term)
        message=f'{search_term}'

        return render(request, 'all_templates/search_results.html', {'message': message, 'images': images})
    else:
        message = 'Not found'
    return render(request, 'all_templates/search_results.html',{"message":message})

