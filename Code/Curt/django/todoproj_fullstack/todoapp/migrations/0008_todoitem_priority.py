# Generated by Django 3.0.4 on 2020-03-05 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_remove_todoitem_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='priority',
            field=models.CharField(choices=[('1', 'Low'), ('2', 'Medium'), ('3', 'High')], default=1, max_length=8),
            preserve_default=False,
        ),
    ]
