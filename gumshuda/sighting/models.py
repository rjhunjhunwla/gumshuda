from django.db import models
from datetime import datetime    

# Create your models here.

class sighting( models.Model ):
    loc = models.CharField( max_length=64 )
    picture_id = models.ForeignKey('picture')

class people( models.Model ):
    name = models.CharField( max_length=256)
    father_name = models.CharField( max_length=256)
    mother_name = models.CharField( max_length=256)
    age = models.IntegerField()
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField()

class picture( models.Model ):
    date = models.DateTimeField(default=datetime.now)
    data = models.BinaryField()
    csum = models.CharField( max_length=1024)

class source_picture( models.Model ):
    people_id = models.ForeignKey('people')
    picture_id = models.ForeignKey('picture')    

class reported_sighting( models.Model ):
    picture_id = models.ForeignKey('picture')
    people_id = models.ForeignKey('people')
    action = models.TextField( )
