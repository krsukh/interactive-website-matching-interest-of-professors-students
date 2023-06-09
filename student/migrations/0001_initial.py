# Generated by Django 4.0.3 on 2022-03-24 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent_research', models.TextField(max_length=150)),
                ('research_abstract', models.TextField(max_length=150)),
                ('scholarship_needed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'StudentProfile',
            },
        ),
    ]
