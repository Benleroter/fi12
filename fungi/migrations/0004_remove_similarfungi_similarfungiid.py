# Generated by Django 3.0 on 2021-10-12 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0003_auto_20211012_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='similarfungi',
            name='SimilarFungiId',
        ),
    ]
