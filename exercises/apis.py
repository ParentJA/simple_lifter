__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Third-party imports...
from rest_framework import generics, mixins

# Local imports...
from .models import Exercise
from .serializers import ExerciseSerializer


class ExerciseAPIView(mixins.RetrieveModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)

        return self.list(request)
