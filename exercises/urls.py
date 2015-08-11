__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.conf import settings
from django.conf.urls import url

# Local imports...
from .apis import ExerciseAPIView

urlpatterns = [
    url(r'^$', ExerciseAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', ExerciseAPIView.as_view()),
]
