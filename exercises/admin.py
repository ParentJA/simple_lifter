__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.contrib import admin

# Local imports...
from .models import Exercise, Force, Mechanics, Muscle, Utility


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    pass


@admin.register(Force)
class ForceAdmin(admin.ModelAdmin):
    pass


@admin.register(Mechanics)
class MechanicsAdmin(admin.ModelAdmin):
    pass


@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    pass


@admin.register(Utility)
class UtilityAdmin(admin.ModelAdmin):
    pass
