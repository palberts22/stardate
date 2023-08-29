from django.shortcuts import render, redirect
from starapp.models import SDate
from django.http import HttpResponse,HttpResponseRedirect
from .forms import StarForm
from django.views.generic.list import ListView
from django.urls import reverse
import pandas as pd

import subprocess
import time
from datetime import datetime, date
import datecalc as datecalc
from tzconversion import tzconvert
from django.contrib.auth.models import User
from .forms import RegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView



# Create your views here.

class AdminLogin(LoginView):
    template_name = "starapp/LoginView_form.html"

@login_required(login_url='login/')
def index(request):
    if request.method == 'POST':
        form = StarForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            bdate = form.cleaned_data['bdate']
            btime = form.cleaned_data['btime']
            startdate = form.cleaned_data['startdate']
            enddate = form.cleaned_data['enddate']
            orb = form.cleaned_data['orb']
            
            request.session['startdatestr'] = str(startdate)
            
            
            
            #redundant lines below, converting django to strings because of legacy flask code
            userid = request.user.id
            SDate.objects.filter(user_id=userid).delete()
            dob = str(bdate)
            enddate = str(enddate)
            btime = str(btime)
            latitude = str(latitude)
            longitude = str(longitude)
            startdate = str(startdate)
            orb = str(orb)
            # end known redundancy

            steps = str(datecalc.calc(dob,enddate))
            
            tzconvert(dob,btime,latitude,longitude,steps,orb, userid)
            return HttpResponseRedirect(reverse('starapp:aspects'))
    else:
        form = StarForm()
    return render(request,'starapp/index.html', {'form': form})
    
# Need to turn into custom view

def AspectsTable(request):
    model= SDate
    userid = request.user.id

    startdatestr = request.session.get('startdatestr')
    startdatestr = str(startdatestr)
    startdate = datetime.strptime(startdatestr, "%Y-%m-%d")
    
    if startdatestr:
        return SDate.objects.filter(date__gte = startdate, user=userid) 
    return SDate.objects.filter(user=userid)


class AspectsView(LoginRequiredMixin, ListView):
    
    
    ##Next two lines are all thats really required if we drop "start date"
    # ordering = ['id_num']
    # context_object_name = 'sdate'
    # queryset = SDate.objects.all()
    ## End this section
    
    ## Paginate turned off, as it breaks the order
    model = SDate
    
    ## Ordering moved to models.py for now
    #ordering = ['date']
    #paginate_by = 365
    def get_queryset(self):
        userid = self.request.user.id

        startdatestr = self.request.session.get('startdatestr')
        startdatestr = str(startdatestr)
        startdate = datetime.strptime(startdatestr, "%Y-%m-%d")
        
        #if startdatestr:
        #    return SDate.objects.filter(date__gte = startdate) 
        #return SDate.objects.all()
        
        if startdatestr:
            return SDate.objects.filter(date__gte = startdate, user=userid) 
        return SDate.objects.filter(user=userid)
         
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "starapp/register.html", {"form":form})