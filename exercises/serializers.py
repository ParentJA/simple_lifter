__author__ = 'jason.a.parent@gmail.com (Jason Parent)'

# Third-party imports...
from rest_framework import serializers

# Local imports...
from .models import Exercise, Force, Mechanics, Muscle, Utility


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
    _utility = UtilitySerializer(source='utility')
    _mechanics = MechanicsSerializer(source='mechanics')
    _force = ForceSerializer(source='force')
    _muscle = MuscleSerializer(source='muscle')

    class Meta:
        model = Exercise
        fields = (
            'id', 'name', '_utility', '_mechanics', '_force', '_muscle', 'preparation', 'execution'
        )
