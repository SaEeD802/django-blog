# Generated by Django 4.1 on 2023-08-28 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_message_age_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 28, 17, 0, 2, 966728, tzinfo=datetime.timezone.utc), verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 28, 17, 0, 2, 968749, tzinfo=datetime.timezone.utc), verbose_name='تاریخ'),
        ),
    ]