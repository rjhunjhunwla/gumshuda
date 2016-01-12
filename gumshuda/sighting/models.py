from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Sighting(models.Model):
    loc = models.CharField(max_length=64)
    picture_id = models.ForeignKey('Picture')


class MissingPerson(models.Model):
    name = models.CharField(max_length=256)
    father_name = models.CharField(max_length=256)
    mother_name = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)  # M,F,U
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=datetime.now)
    reporting_user_id = models.ForeignKey(User)
    person_group_id = models.CharField(max_length=256)
    metadata = models.CharField(max_length=1024)
    missing_or_found = models.BooleanField(default=True) #True means missing, false means reported found


class Picture(models.Model):
    date = models.DateTimeField(default=datetime.now)
    data = models.BinaryField()
    csum = models.CharField(max_length=1024)
    prop = models.TextField()
    face_id = models.CharField(max_length=256)


class SourcePicture(models.Model):
    missing_person_id = models.ForeignKey('MissingPerson')
    picture_id = models.ForeignKey('Picture')
    face_id = models.CharField(max_length=256, null=False)



class ReportedSighting(models.Model):
    picture_id = models.ForeignKey('Picture')
    missing_person_id = models.ForeignKey('MissingPerson')
    action = models.TextField()
    reporting_user_id = models.IntegerField()
