# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-01 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0021_auto_20171002_0038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Notification', models.CharField(default='', max_length=300)),
                ('Batch', models.CharField(choices=[('Ceramic Engineering', 'Ceramic Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Electronics Engineering', 'Electronics Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering', 'Metallurgical Engineering'), ('Mining Engineering', 'Mining Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Pharmaceutical Engineering', 'Pharmaceutical Engineering'), ('Material Science and Technology', 'Material Science and Technology'), ('Biochemical Engineering', 'Biochemical Engineering'), ('Biomedical Engineering', 'Biomedical Engineering'), ('Department of Chemistry', 'Department of Chemistry'), ('Department of Physics', 'Department of Physics'), ('Department of Mathematical Sciences', 'Department of Mathematical Sciences')], default='None', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
