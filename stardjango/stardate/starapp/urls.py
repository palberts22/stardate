from django.urls import path
import starapp
from starapp.views import AspectsView

app_name = 'starapp'
urlpatterns = [
    path('', starapp.views.index, name='index'),
    path('aspects/', AspectsView.as_view(), name="aspects"),
]