from __future__ import unicode_literals

from django.db import models

# Create your models here.

address_item = ((0,'good'),(1,'Average'),(2,'Bad'))



class Movie(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)
    duration = models.IntegerField(blank=True,null=True)
    review = models.IntegerField(choices = address_item, blank=True, null=True)
    rating = models.FloatField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.name