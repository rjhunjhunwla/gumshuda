from django.db import models
from datetime import datetime    

# Create your models here.

class sighting( models.Model ):
	loc = models.CharField( max_length=64 )
	date = models.DateTimeField(default=datetime.now)
	data = models.BinaryField()
	csum = models.CharField( max_length=1024)

class people( models.Model ):
    name = models.CharField( max_length=256)
    father_name = models.CharField( max_length=256)
    mother_name = models.CharField( max_length=256)
    age = models.IntegerField()
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField()