# Generated by Django 3.2.9 on 2021-12-03 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=50)),
                ('company_email', models.EmailField(max_length=50)),
                ('linkedin_url', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('job_title', models.CharField(default='', max_length=50)),
                ('job_location', models.CharField(max_length=20)),
                ('job_description', models.TextField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('posted_at', models.DateField(auto_now=True)),
                ('deadline_at', models.DateField()),
                ('company', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jobmanagers.company')),
            ],
        ),
    ]
