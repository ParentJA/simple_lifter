__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Third-party imports...
from rest_framework import status, views
from rest_framework.response import Response

# Local imports...
from .models import Exercise, WorkoutExercise
from .serializers import (
    ExerciseSerializer, ForceSerializer, MechanicsSerializer, MuscleSerializer, UtilitySerializer, WorkoutSerializer,
    WorkoutExerciseSerializer
)


class ExerciseAPIView(views.APIView):
    def get(self, request, pk=None):
        exercises = Exercise.objects.select_related()

        if pk:
            exercises = exercises.filter(pk=pk)

        # Extract the utilities...
        utilities = set([exercise.utility for exercise in exercises])

        # Extract the mechanics...
        mechanics = set([exercise.mechanics for exercise in exercises])

        # Extract the forces...
        forces = set([exercise.force for exercise in exercises])

        # Extract the muscles...
        muscles = set([exercise.muscle for exercise in exercises])

        return Response(status=status.HTTP_200_OK, data={
            'exercises': ExerciseSerializer(exercises, many=True).data,
            'utilities': UtilitySerializer(utilities, many=True).data,
            'mechanics': MechanicsSerializer(mechanics, many=True).data,
            'forces': ForceSerializer(forces, many=True).data,
            'muscles': MuscleSerializer(muscles, many=True).data
        })


class WorkoutAPIView(views.APIView):
    def get(self, request, pk=None):
        workout_exercises = WorkoutExercise.objects.select_related()

        if pk:
            workout_exercises = workout_exercises.filter(pk=pk)

        # Extract the workouts...
        workouts = set([workout_exercise.workout for workout_exercise in workout_exercises])

        # Extract the exercises...
        exercises = set([workout_exercise.exercise for workout_exercise in workout_exercises])

        # Extract the utilities...
        utilities = set([exercise.utility for exercise in exercises])

        # Extract the mechanics...
        mechanics = set([exercise.mechanics for exercise in exercises])

        # Extract the forces...
        forces = set([exercise.force for exercise in exercises])

        # Extract the muscles...
        muscles = set([exercise.muscle for exercise in exercises])

        return Response(status=status.HTTP_200_OK, data={
            'workouts': WorkoutSerializer(workouts, many=True).data,
            'workout_exercises': WorkoutExerciseSerializer(workout_exercises, many=True).data,
            'exercises': ExerciseSerializer(exercises, many=True).data,
            'utilities': UtilitySerializer(utilities, many=True).data,
            'mechanics': MechanicsSerializer(mechanics, many=True).data,
            'forces': ForceSerializer(forces, many=True).data,
            'muscles': MuscleSerializer(muscles, many=True).data
        })
