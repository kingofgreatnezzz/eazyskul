from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from django.contrib.auth.decorators import login_required
from .models import *
from imt.models import *
from imt.forms import *
from .forms import *
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import forms
from django.contrib import messages
#from django.contrib.auth.decorators import login_required



#@login_required
def hall_list(request, hall_slug=None):
    results = []
    query = None
    if 'query' in request.GET:
        query = request.GET['query']
        search_vector = SearchVector('name', weight='A') + SearchVector('image1', weight='B')
        search_query = SearchQuery(query)
        results = Sub_Hall.objects.annotate(search = search_vector, rank=SearchRank(search_vector, search_query)
        ).filter(rank__gte=0.3).order_by('-rank')

    if request.method != 'POST':
        hall = None
        halls = Hall.objects.all()
        sub_halls = Sub_Hall.objects.filter(available=True)
        if hall_slug:
            hall = get_object_or_404(Hall, slug=hall_slug)
            sub_halls = sub_halls.filter(hall=hall)
    context = {'hall':hall, 'halls':halls, 'sub_halls':sub_halls,
    'query':query, 'results':results}
    return render(request, 'halls.html', context)


#@login_required
def hall_detail(request, id, slug):
    sub_hall = get_object_or_404(Sub_Hall, slug=slug, id=id, available=True)

    return render(request, 'orientation_copy.html', {'sub_hall':sub_hall})


 
def  kga(request):
    kga1 = kgaa.objects.all()

    return render(request,'projects/greatness_art.html',{
        'kga1': kga1,
    })


# howto page 
#@login_required
def howto(request):
    how_picz1 = how_picz.objects.all()
    how = howtoz.objects.all()
    if request.method == 'POST':
        regu = RegularForm(request.POST)
        if regu.is_valid():
            regu.save()
            messages.success(request,"you'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/howto.html", {'regu': regu})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, regu.errors)
    else: 
        regu = RegularForm()
            
    return render(request,"projects/howto.html", {
        "how " : how,
        "how_picz1" : how_picz1,
        "regu": regu,
   })    


#clearance page
#@login_required
def clearance(request):
    clearances1 = clearances_expalain.objects.all()
    clearancepicz1 = clearancepicz.objects.all() 
    if request.method == 'POST':
        clearform = ClearanceForm(request.POST)
        if clearform.is_valid():
            clearform.save()
            messages.success(request,"you'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/clearance.html", {'clearform': clearform})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, clearform.errors)
    else: 
        clearform = ClearanceForm()

    return render(request,"projects/clearance.html", {
        " clearances1" :  clearances1, 
        "clearform" : clearform,
        "clearancepicz1": clearancepicz1, 
    })

#registration page 
#@login_required
def reg_page(request):
    registrations1 = reg_ex.objects.all()
    reg_pics1 = regista_pics.objects.all()
    if request.method == 'POST':
        regform = RegistrationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request,"you'll get a response in not less than 24 hours. Please check your mails to avoid missing communication. Thanks")
            return render(request, "projects/registration.html", {'regform': regform})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, regform.errors)
    else: 
        regform = RegistrationForm()
            

    return render(request,"projects/registration.html", {
        "registrations1" :  registrations1,
        'reg_pics1': reg_pics1,
        "regform" : regform,
    })    

