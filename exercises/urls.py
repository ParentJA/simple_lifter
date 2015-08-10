__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Django imports...
from django.conf import settings
from django.conf.urls import url

# Local imports...
from .apis import ExerciseViewSet

urlpatterns = [
    url(r'^$', ExerciseViewSet.as_view(settings.REST_METHODS)),
    url(r'^(?P<pk>\d+)/$', ExerciseViewSet.as_view(settings.REST_METHODS_PK)),
]
