# Generated by Django 3.0.4 on 2020-03-10 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('choirapp', '0005_auto_20200310_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='comp_last',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='composition', to='choirapp.Composer', verbose_name='Composer'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='turn_in_date',
            field=models.DateField(),
        ),
    ]