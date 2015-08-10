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
                ('utility', models.CharField(max_length=250)),
                ('mechanics', models.CharField(max_length=250)),
                ('force', models.CharField(max_length=250)),
                ('muscle', models.CharField(max_length=250)),
                ('preparation', models.TextField()),
                ('execution', models.TextField()),
            ],
        ),
    ]
