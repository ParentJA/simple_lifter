__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.conf import settings
from django.conf.urls import url

# Local imports...
from .apis import ExerciseAPIView, WorkoutAPIView

urlpatterns = [
    url(r'^exercises/$', ExerciseAPIView.as_view()),
    url(r'^exercises/(?P<pk>\d+)/$', ExerciseAPIView.as_view()),
    url(r'^workouts/$', WorkoutAPIView.as_view()),
    url(r'^workouts/(?P<pk>\d+)/$', WorkoutAPIView.as_view()),
]
