# Generated by Django 3.0 on 2021-11-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0008_auto_20211109_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='showgroup',
            name='GroupCheck',
            field=models.BooleanField(default=False, verbose_name=' _group_check'),
        ),
    ]
