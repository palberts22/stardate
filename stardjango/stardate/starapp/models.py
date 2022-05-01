from django.db import models

# Create your models here.
# CREATE TABLE consolidated_aspects(
#     id int PRIMARY KEY,
#     date timestamptz,
#     aspects text

class SDate(models.Model):
    id_num = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    aspects = models.CharField(max_length=2048)
    def __str__(self):
        return '%s %s %s' % (self.id_num, self.date, self.aspects)
    class Meta:
        ordering = ['date']
    
# from django.contrib.auth import get_user_model
# for each authenticated user, create a table for them to store ephem data