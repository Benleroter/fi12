# Generated by Django 3.0 on 2021-11-09 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usersettings', '0007_auto_20211109_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showgroup',
            name='user',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='user_group', to=settings.AUTH_USER_MODEL),
        ),
    ]
