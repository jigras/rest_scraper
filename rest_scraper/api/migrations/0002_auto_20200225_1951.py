# Generated by Django 3.0.3 on 2020-02-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Tekst ze strony'),
        ),
    ]
