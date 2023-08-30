# Generated by Django 4.1 on 2023-08-29 11:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 29, 11, 39, 49, 549390, tzinfo=datetime.timezone.utc), verbose_name='تاریخ انتشار'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 29, 11, 39, 49, 551389, tzinfo=datetime.timezone.utc), verbose_name='تاریخ'),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='پسندیده شده در')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blog.article', verbose_name='مقاله')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'لایک',
                'verbose_name_plural': 'لایک ها',
                'ordering': ('-created_at',),
            },
        ),
    ]
