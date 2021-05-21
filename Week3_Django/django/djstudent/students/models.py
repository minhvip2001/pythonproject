from django.db import models

# Create your models here.
from django.forms import ModelForm, Textarea
from django.db import models

class Students(models.Model):
  sId = models.IntegerField(primary_key=True)
  f_name = models.CharField(max_length=100)
  l_name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  class Meta:
    db_table = 'students' 
