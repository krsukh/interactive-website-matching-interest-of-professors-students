# Generated by Django 4.0.3 on 2022-03-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='research_lab',
            field=models.TextField(blank=True, max_length=5, null=True),
        ),
    ]
