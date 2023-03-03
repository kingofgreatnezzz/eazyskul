from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from halls.models import *
from django.contrib.auth import forms
from django.contrib import messages

from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here 

# login page 
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/index')
                else:
                    return HttpResponse('Disabled account')
            else:
                messages.info(request,'Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

#register function 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'projects/index.html',{'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,'registration/signup.html',{'user_form': user_form})
   
#exam page
#@login_required
def exam(request):
    exform = examzForm
    if request.method == 'POST':
        exform = examzForm(request.POST)
        if exform.is_valid():
            exform.save()
            messages.success(request,'form has been create successfully')
            return redirect('/message_successful')
    return render(request,"projects/exam.html", {
        "exform": exform,
    }) 

#contactz_form function 
def contact(request):
    contformz = ContactzForm
    cont1 = contact_info.objects.all()
    if request.method == 'POST':
        contformz = ContactzForm(request.POST)
        if contformz.is_valid():
            contformz.save()
            messages.success(request,'form has been create successfully')
            return redirect('/message_successful')

    return render(request,"projects/contact.html", {
        "contformz": contformz, 
        "cont1" : cont1
        })

#form_group page 
def form_group(request):
    formz = GroupFormProject
    if request.method == 'POST':
        group_forms = GroupFormProject(request.POST)
        if group_forms.is_valid():
            group_forms.save()
            messages.success(request,'form has been create successfully')
            return redirect('/message_successful')
    return render(request,"form_group.html", {"formz": formz})    


def index(request):
    hm_picz = home_img.objects.all()

    return render(request,"projects/index.html",
    {
        "hm_picz" : hm_picz,
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

#project page
#@login_required 
def project(request):
    return render(request,"projects/project.html")    

# pd page 
#@login_required
def PD(request):
    pd1= pd.objects.all()
    return render(request,"projects/PD.html",{
        "pd1" :pd1
    })


def terms_condition(request):
    return render(request, 'projects/terms_condition.html')

def errorpage(request):
    return render(request,"errorpage.html")  

def message_successful(request):
    return render(request, "message_successful.html")