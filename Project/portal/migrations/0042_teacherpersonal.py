# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-10-29 10:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0041_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[(b'Associate Professor', b'Associate Professor'), (b'Assistant Professor', b'Assistant Professor'), (b'Professor', b'Professor')], default=b'B.Tech', max_length=100, null=True)),
                ('adminPos', models.CharField(choices=[(b'None', b'None'), (b'Director', b'Director'), (b'Dean of Academic Affairs', b'Dean of Academic Affairs'), (b'Associate Dean of Academic Affairs', b'Associate Dean of Academic Affairs'), (b'Dean of Student Affairs', b'Dean of Student Affairs'), (b'Dean of Resource and Alumni', b'Dean of Resource and Alumni'), (b'Dean of Research and Development', b'Dean of Research and Development'), (b'Registrar', b'Registrar'), (b'Professor Incharge(Faculty Affairs)', b'Professor Incharge(Faculty Affairs)')], default=b'Ceramic Engineering', max_length=100, null=True)),
                ('interest', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=100)),
                ('image', models.FileField(blank=True, null=True, upload_to=b'')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
