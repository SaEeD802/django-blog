# Generated by Django 4.1 on 2023-07-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='موضوع')),
                ('text', models.TextField(verbose_name='متن')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
            ],
        ),
    ]