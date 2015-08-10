__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=250)
    utility = models.CharField(max_length=250)
    mechanics = models.CharField(max_length=250)
    force = models.CharField(max_length=250)
    muscle = models.CharField(max_length=250)
    preparation = models.TextField()
    execution = models.TextField()

    def __unicode__(self):
        return self.name
