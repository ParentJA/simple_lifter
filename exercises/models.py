__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=250)
    utility = models.ForeignKey('exercises.Utility', related_name='exercises')
    mechanics = models.ForeignKey('exercises.Mechanics', related_name='exercises')
    force = models.ForeignKey('exercises.Force', related_name='exercises')
    muscle = models.ForeignKey('exercises.Muscle', related_name='exercises')
    preparation = models.TextField()
    execution = models.TextField()

    def __unicode__(self):
        return self.name


class Utility(models.Model):
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'utilities'

    def __unicode__(self):
        return self.description


class Mechanics(models.Model):
    description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'mechanics'

    def __unicode__(self):
        return self.description


class Force(models.Model):
    description = models.CharField(max_length=250)

    def __unicode__(self):
        return self.description


class Muscle(models.Model):
    description = models.CharField(max_length=250)

    def __unicode__(self):
        return self.description
