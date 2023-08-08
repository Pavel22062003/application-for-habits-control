# Generated by Django 4.2.3 on 2023-08-04 12:05

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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(verbose_name='место в котором нужно выполнить привычку')),
                ('time', models.TimeField(verbose_name='время, когда необходимо выполнять привычку')),
                ('action', models.CharField(verbose_name='действие, которое нужно выполнить')),
                ('sign', models.BooleanField(verbose_name='признак приятной привычки')),
                ('periodicity', models.IntegerField(default=1, verbose_name='периодичность')),
                ('reward', models.CharField(verbose_name='награда')),
                ('time_to_complete', models.TimeField(verbose_name='время на выполнение')),
                ('publicity', models.BooleanField(default=True, verbose_name='признак публичности')),
                ('connected_habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='habits.habit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]