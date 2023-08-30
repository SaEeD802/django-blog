# Generated by Django 4.1 on 2023-07-14 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0, verbose_name='سن'),
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 14, 17, 18, 24, 914913, tzinfo=datetime.timezone.utc), verbose_name='تاریخ'),
        ),
    ]
