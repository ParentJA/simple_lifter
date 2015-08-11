# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('preparation', models.TextField()),
                ('execution', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Force',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'mechanics',
            },
        ),
        migrations.CreateModel(
            name='Muscle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'utilities',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutExercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exercise', models.ForeignKey(related_name='workout_exercises', to='exercises.Exercise')),
                ('workout', models.ForeignKey(related_name='workout_exercises', to='exercises.Workout')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='force',
            field=models.ForeignKey(related_name='exercises', to='exercises.Force'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='mechanics',
            field=models.ForeignKey(related_name='exercises', to='exercises.Mechanics'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='muscle',
            field=models.ForeignKey(related_name='exercises', to='exercises.Muscle'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='utility',
            field=models.ForeignKey(related_name='exercises', to='exercises.Utility'),
        ),
    ]
