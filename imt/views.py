from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from halls.models import *
from django.contrib import auth ,messages
from django.contrib.auth import forms
from django.contrib.auth.decorators import login_required
# Create your views here 
from .forms import *
from django.shortcuts import render, get_object_or_404
#def index(request):

def index(request):
    hm_picz = home_img.objects.all()
    return render(request,  'projects/index.html' ,{
        "hm_picz" : hm_picz,
        })


# Create your views here 
#login page
def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request,user)
                messages.success(request, 'You are now logged in')
                return redirect('index') 
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('index')
        else:
            return render(request, 'registration/login.html', {})

#register function 
def register(request):
    user_form = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('login')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already taken')
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username,email=email, password=password)
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')  
            return HttpResponseRedirect('register') 
            # return redirect('register')
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/signup.html',{'user_form': user_form})


#exam page
#@login_required
def exam(request):
    if request.method == 'POST':
        exform = examzForm(request.POST)
        if exform.is_valid():
            exform.save()
            messages.success(request,"you'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/exam.html", {'exform': exform})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, exform.errors)
    else: 
        exform = examzForm()
           
    return render(request,"projects/exam.html", {
        "exform": exform,
    }) 

#contactz_form function 
def contact(request):
    if request.method == 'POST':
        contformz = ContactzForm(request.POST)
        if contformz.is_valid():
            contformz.save()
            messages.success(request,"you'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/contact.html", {'contformz': contformz})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, contformz.errors)
    else: 
        contformz = ContactzForm()
            

    return render(request,"projects/contact.html", {
        "contformz": contformz, 
        })

#project page
#@login_required 
def project(request):
    if request.method == 'POST':
        profom = GroupFormProject(request.POST)
        if profom.is_valid():
            profom.save()
            messages.success(request,"you'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/project.html", {'profom': profom})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, profom.errors)
    else: 
        profom = GroupFormProject()
            
    return render(request,"projects/project.html", {
        "profom": profom, 
        })    

#about page
def about(request):
    abt1 = about_picz_memebers.objects.all()
    return render(request, "projects/about.html", {
        "abt1": abt1
    })

#work  (EAZY SKULL) page  AT     
def work(request):
    work1 = workz.objects.all()

    return render(request,"projects/work.html", {
        "work1" : work1
    })

# pd page 
#@login_required
def PD(request):
    pd1= pd.objects.all()
    return render(request,"projects/PD.html",{
        "pd1" :pd1
    })

def terms_condition(request):
    return render(request, 'projects/terms_condition.html')