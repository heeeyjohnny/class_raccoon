# Generated by Django 3.0.2 on 2020-02-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshorten', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlshorten',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
