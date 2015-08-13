# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_reps', models.IntegerField()),
                ('max_reps', models.IntegerField()),
                ('workout_exercise', models.ForeignKey(related_name='sets', to='exercises.WorkoutExercise')),
            ],
        ),
    ]
