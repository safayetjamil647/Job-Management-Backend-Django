# Generated by Django 3.2.9 on 2021-12-04 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobmanagers', '0002_job_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jobmanagers.company'),
        ),
    ]