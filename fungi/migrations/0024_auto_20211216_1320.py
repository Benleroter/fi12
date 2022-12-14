# Generated by Django 3.0 on 2021-12-16 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0023_auto_20211215_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fungi',
            name='CommonName',
            field=models.CharField(default='Common Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='fungi',
            name='LatinName',
            field=models.CharField(default='Latin Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='gills',
            name='GillsPresent',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='poresandtubes',
            name='PoresPresent',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20, null=True),
        ),
    ]
