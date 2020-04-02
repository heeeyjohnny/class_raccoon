# Generated by Django 3.0.4 on 2020-03-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('choirapp', '0014_rehearsal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rehearsal',
            name='reh_date',
        ),
        migrations.RemoveField(
            model_name='rehearsal',
            name='updated',
        ),
        migrations.AlterField(
            model_name='composition',
            name='location',
            field=models.CharField(blank=True, default='Stacks', max_length=30, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='voicing',
            field=models.CharField(blank=True, default='SATB', max_length=20, null=True, verbose_name='Voicing'),
        ),
    ]