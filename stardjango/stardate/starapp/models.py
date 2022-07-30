from django.db import models
from django.contrib.auth.models import User
#from django.conf import settings
#from django.db.models.signals import post_save
# Create your models here.
# CREATE TABLE consolidated_aspects(
#     id int PRIMARY KEY,
#     date timestamptz,
#     aspects text

class SDate(models.Model):
    user = models.ForeignKey(User, default='0', on_delete=models.CASCADE, null=True, blank=True) 
    #id_num = models.AutoField(primary_key=True)
    #id_num = models.AutoField()
    date = models.DateTimeField()
    aspects = models.TextField(max_length=6000)
    def __str__(self):
        return '%s %s %s' % (self.user, self.date, self.aspects)
    class Meta:
        ordering = ['date']
        
    
# from django.contrib.auth import get_user_model
# for each authenticated user, create a table for them to store ephem data
    
