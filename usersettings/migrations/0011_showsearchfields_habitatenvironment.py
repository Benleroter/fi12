# Generated by Django 3.0 on 2022-08-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersettings', '0010_auto_20211111_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='showsearchfields',
            name='HabitatEnvironment',
            field=models.BooleanField(default=False, verbose_name=' _Environment'),
        ),
    ]