from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime 
from . models import Futsalbookingdetail, Futsal
from .forms import FutsalForm, FutsalbookingdetailForm
from django.http import HttpResponseRedirect

def futsalbooking_add(request):
    submitted = False
    if request.method == "POST":
        form =  FutsalbookingdetailForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/futsalbooking_add?submitted=True')
    else:
        form = FutsalbookingdetailForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'futsal_name/futsalbooking_add.html', {"form":form, "submitted":submitted,})


def futsals_update(request, futsal_id):
    futsal = Futsal.objects.get(pk=futsal_id)
    form = FutsalForm(request.POST or None, instance=futsal)
    if form.is_valid():
        form.save()
        return redirect('futsals_list')
    return render(request, 'futsal_name/futsal_update.html', {"futsal":futsal, "form":form,})


def futsals_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        futsals = Futsal.objects.filter(name__contains=searched)
        return render(request, 'futsal_name/futsal_search.html', {"searched":searched, "futsals":futsals,})
    else:
        return render(request, 'futsal_name/futsal_search.html', {})



def futsals_show(request, futsal_id):
    futsal = Futsal.objects.get(pk=futsal_id)
    return render(request, 'futsal_name/futsal_show.html', {"futsal":futsal,})

def all_futsals_list(request):
    futsal_list = Futsal.objects.all()
    return render(request, 'futsal_name/futsal_list.html', {"futsal_list":futsal_list,})

def add_futsal(request):
    submitted = False
    if request.method == "POST":
        form = FutsalForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_futsal?submitted=True')
    else:
        form = FutsalForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'futsal_name/add_futsal.html', {"form":form, "submitted":submitted,})


def all_futsalbooking_list(request):
    booking_list = Futsalbookingdetail.objects.all()
    return render(request, 'futsal_name/futsalbooking_list.html', {
        "booking_list":booking_list,
    })

# Create your views here.

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "asmin"
    location = "sitapaila"
    month = month.capitalize()
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    #create calener 
    cal = HTMLCalendar().formatmonth(
        year,
        month_number,)
    
    #get current year 
    now = datetime.now()
    current_year = now.year


    #GET CURRENT TIME
    time = now.strftime('%I:%M:%S %p')

    return render(request, 
                  'futsal_name/home.html', {
                      'name': name, 
                      'location': location, 
                      'year':year,
                      'month': month,
                      "month_number": month_number,
                      "cal":cal,
                      "current_year":current_year,
                      "time":time,
                      }) 


