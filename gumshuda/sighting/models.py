from django.db import models

# Create your models here.

class sighting( models.Model ):
	loc = models.CharField( max_length=64 )
	date = models.DateTimeField('date queried')
	data = models.BinaryField()