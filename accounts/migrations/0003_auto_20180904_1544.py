# Generated by Django 2.0.4 on 2018-09-04 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180904_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(default='', max_length=500),
        ),
    ]