__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Third-party imports...
from rest_framework import serializers

# Local imports...
from .models import Exercise, Force, Mechanics, Muscle, Utility, Workout, WorkoutExercise


class UtilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Utility
        fields = ('id', 'description')


class MechanicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanics
        fields = ('id', 'description')


class ForceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Force
        fields = ('id', 'description')


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ('id', 'description')


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = (
            'id', 'name', 'utility', 'mechanics', 'force', 'muscle', 'preparation', 'execution'
        )


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'name')


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutExercise
        fields = ('id', 'workout', 'exercise')
