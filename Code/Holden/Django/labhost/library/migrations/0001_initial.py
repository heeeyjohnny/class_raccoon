# Generated by Django 3.0.2 on 2020-02-17 23:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('year_published', models.IntegerField()),
                ('authors', models.ManyToManyField(related_name='books', to='library.Author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BookCheckout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(null=True)),
                ('checkin_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='copies', to='library.Book')),
                ('checked_out_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='checkouts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('checkout_date', models.DateTimeField()),
                ('checkin_date', models.DateTimeField()),
                ('book_copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkout_history', to='library.BookCheckout')),
            ],
            options={
                'ordering': ['checkin_date'],
            },
        ),
    ]
