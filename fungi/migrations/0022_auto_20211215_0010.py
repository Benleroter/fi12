# Generated by Django 3.0 on 2021-12-15 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0021_auto_20211212_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gills',
            name='GillsPresent',
            field=models.CharField(blank=True, choices=[('initial', ''), ('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, null=True),
        ),
    ]
