# Generated by Django 4.2.3 on 2023-08-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='chat_id телеграм'),
        ),
    ]
