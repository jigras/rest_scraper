# Generated by Django 3.0.3 on 2020-02-25 19:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200225_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='picture',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
