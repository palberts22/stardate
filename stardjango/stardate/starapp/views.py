from django.shortcuts import render
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




# Create your views here.
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
            dob = str(bdate)
            enddate = str(enddate)
            btime = str(btime)
            latitude = str(latitude)
            longitude = str(longitude)
            startdate = str(startdate)
            orb = str(orb)
            # end known redundancy

            steps = str(datecalc.calc(dob,enddate))
            tzconvert(dob,btime,latitude,longitude,steps,orb)
            return HttpResponseRedirect(reverse('starapp:aspects'))
    else:
        form = StarForm()
    return render(request,'starapp/index.html', {'form': form})
    
# Need to turn into custom view

class AspectsView(ListView):
    
    
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
        startdatestr = self.request.session.get('startdatestr')
        startdatestr = str(startdatestr)
        startdate = datetime.strptime(startdatestr, "%Y-%m-%d")
        
        if startdatestr:
            return SDate.objects.filter(date__gte = startdate) 
        return SDate.objects.all()
         
   