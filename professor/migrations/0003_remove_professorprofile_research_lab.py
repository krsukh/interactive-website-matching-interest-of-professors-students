# Generated by Django 4.0.3 on 2022-03-24 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professorprofile',
            name='research_lab',
        ),
    ]
