from django import forms
import datetime as dt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StarForm(forms.Form):
    name = forms.CharField(label='Name', max_length = 100)
    address = forms.CharField(label = 'Where were you born?')
    latitude = forms.DecimalField(label = 'Latitude')
    longitude = forms.DecimalField(label = 'Longitude')
    bdate = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')), label = 'Birthday')
    btime = forms.TimeField(widget=forms.TimeInput(attrs=dict(type='time')), label = 'Birth Time')
    orb = forms.IntegerField(label = 'Orb of conjunction', initial = 7)
    # Need to implement startdate for results view
    startdate = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')), label = 'Start display date', initial=dt.date.today)
    delta = dt.datetime.now() + dt.timedelta(days=365)
    datedelta = dt.datetime.date(delta)
    enddate = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')), label = 'End display date', initial= datedelta)

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]