# Generated by Django 3.0.3 on 2020-02-27 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200225_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(help_text='Adres url strony z protokołem http/https', max_length=2048, verbose_name='Url strony'),
        ),
    ]