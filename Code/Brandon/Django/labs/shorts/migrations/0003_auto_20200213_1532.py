# Generated by Django 3.0.2 on 2020-02-13 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorts', '0002_shorten_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorten',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]