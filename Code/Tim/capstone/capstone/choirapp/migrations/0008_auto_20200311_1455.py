# Generated by Django 3.0.4 on 2020-03-11 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choirapp', '0007_auto_20200311_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='turn_in_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]