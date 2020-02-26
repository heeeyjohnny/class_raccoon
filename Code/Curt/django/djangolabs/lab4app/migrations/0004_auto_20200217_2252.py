# Generated by Django 3.0.2 on 2020-02-17 22:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lab4app', '0003_auto_20200217_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='checked_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkouts', to='lab4app.Book'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='checked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkouts', to=settings.AUTH_USER_MODEL),
        ),
    ]
