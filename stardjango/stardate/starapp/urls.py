from django.urls import path
import starapp
from starapp.views import AspectsView
from starapp.views import AdminLogin

app_name = 'starapp'
urlpatterns = [
    path('', starapp.views.index, name='index'),
    path('login/', AdminLogin.as_view(), name='login'),
    path('aspects/', AspectsView.as_view(), name="aspects"),
    
]