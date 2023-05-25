# Generated by Django 4.0.3 on 2022-03-24 09:05

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_professor', models.BooleanField(default=False)),
                ('domestic_country', models.CharField(choices=[('USA', 'USA'), ('CANADA', 'Canada'), ('UK', 'UK'), ('INDIA', 'India'), ('GERMANY', 'Germany'), ('FRANCE', 'France'), ('AUSTRALIA', 'Australia')], max_length=255)),
                ('preferred_study_destination', models.CharField(choices=[('USA', 'USA'), ('CANADA', 'Canada'), ('UK', 'UK'), ('INDIA', 'India'), ('GERMANY', 'Germany'), ('FRANCE', 'France'), ('AUSTRALIA', 'Australia')], max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_of_education', models.CharField(blank=True, choices=[('USA', 'USA'), ('CANADA', 'Canada'), ('UK', 'UK'), ('INDIA', 'India'), ('GERMANY', 'Germany'), ('FRANCE', 'France'), ('AUSTRALIA', 'Australia')], max_length=255, null=True)),
                ('university', models.CharField(choices=[('Massachusetts Institute of Technology (MIT)', 'Massachusetts Institute of Technology (MIT)'), ('University of Oxford', 'University of Oxford'), ('University of Chicago', 'University of Chicago'), ('University of Toronto', 'University of Toronto'), ('Ruprecht-Karls-Universitat Heidelberg', 'Ruprecht-Karls-Universitat Heidelberg'), ('Monash University', 'Monash University'), ('University of Delhi', 'University of Delhi'), ('Lovely Professional University', 'Lovely Professional University')], max_length=255)),
                ('department', models.CharField(choices=[('BCA', 'BCA'), ('Bsc', 'Bsc'), ('BTech', 'BTech'), ('MCA', 'MCA'), ('MSc', 'MSc'), ('MTech', 'MTech'), ('IT', 'IT')], max_length=255)),
                ('specialization', models.CharField(choices=[('Analytical Chemistry', 'Analytical Chemistry'), ('Organic Chemistry', 'Organic Chemistry'), ('Biotechnology', 'Biotechnology'), ('Materials & Textiles', 'Materials & Textiles'), ('Technical Support', 'Technical Support'), ('Technical Communication/Science Writing', 'Technical Communication/Science Writing'), ('Human Resources', 'Human Resources')], max_length=255)),
                ('degree_level', models.CharField(blank=True, choices=[('Diploma', 'Diploma'), ('Bachelor', 'Bachelor'), ('Post Graduate', 'Post Graduate'), ('Masters', 'Masters')], max_length=255, null=True)),
                ('degree_name', models.CharField(blank=True, max_length=50, null=True)),
                ('course_start_date', models.DateField()),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('gpa', models.TextField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Education',
            },
        ),
    ]