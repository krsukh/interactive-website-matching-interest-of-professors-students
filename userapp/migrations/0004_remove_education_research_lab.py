# Generated by Django 4.0.3 on 2022-03-24 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_education_research_lab'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='research_lab',
        ),
    ]