# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-30 11:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0016_status_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='None', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='subject1',
            field=models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject2',
            field=models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject3',
            field=models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='summer',
            name='subject1',
            field=models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='summer',
            name='subject2',
            field=models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='summer',
            name='subject3',
            field=models.CharField(choices=[('None', 'None'), ('MA202: Statistics and Probability', 'MA202: Statistics and Probability'), ('CSO211: Computer System Organization', 'CSO211: Computer System Organization'), ('CSO204: Discrete Maths', 'CSO204: Discrete Maths'), ('ME104: Engineering Mechanics', 'ME104: Engineering Mechanics'), ('H105: Philosophy', 'H105: Philosophy'), ('MA101: Engineering Mathematics-I', 'MA101: Engineering Mathematics-I'), ('MA102: Engineering Mathematics-II', 'MA102: Engineering Mathematics-II'), ('CSO101: Introduction to Computer Programming', 'CSO101: Introduction to Computer Programming'), ('CSO102: Data Structures', 'CSO102: Data Structures'), ('EO101: Fundamentals of Electrical Engineering', 'EO101: Fundamentals of Electrical Engineering'), ('PHY101: Physics - Classical, Quantum and Relativistic', 'PHY101: Physics - Classical, Quantum and Relativistic'), ('PHY102: Physics - Electrodynamics', 'PHY102: Physics - Electrodynamics'), ('CY101: Chemistry', 'CY101: Chemistry'), ('CSE105: Information Technology Workshop-I', 'CSE105: Information Technology Workshop-I'), ('CSE205: Information Technology Workshop-II', 'CSE205: Information Technology Workshop-II'), ('H104: History and Civilization', 'H104: History and Civilization'), ('H103: Education and Self', 'H103: Education and Self'), ('H102: Development of Societies', 'H102: Development of Societies'), ('H101: Universal Human Values', 'H101: Universal Human Values')], default='', max_length=100),
        ),
    ]
