from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Sighting(models.Model):
    loc = models.CharField(max_length=64)
    picture_id = models.ForeignKey('Picture')


class People(models.Model):
    name = models.CharField(max_length=256)
    father_name = models.CharField(max_length=256)
    mother_name = models.CharField(max_length=256)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)  # M,F,U
    status = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=datetime.now)
    reporting_user_id = models.ForeignKey(User)


class Picture(models.Model):
    date = models.DateTimeField(default=datetime.now)
    data = models.BinaryField()
    csum = models.CharField(max_length=1024)
    prop = models.TextField()


class SourcePicture(models.Model):
    people_id = models.ForeignKey('People')
    picture_id = models.ForeignKey('Picture')


class ReportedSighting(models.Model):
    picture_id = models.ForeignKey('Picture')
    people_id = models.ForeignKey('People')
    action = models.TextField()
    reporting_user_id = models.IntegerField()
