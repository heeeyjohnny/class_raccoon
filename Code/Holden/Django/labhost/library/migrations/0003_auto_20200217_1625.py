# Generated by Django 3.0.2 on 2020-02-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200217_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcheckout',
            name='checkout_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
