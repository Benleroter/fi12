# Generated by Django 3.0 on 2022-09-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0036_auto_20220905_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fungi',
            name='GenusEnglish',
        ),
        migrations.RemoveField(
            model_name='fungi',
            name='GenusLatin',
        ),
        migrations.AddField(
            model_name='fungi',
            name='UKSpecies',
            field=models.CharField(blank=True, choices=[('initial', ''), ('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20, null=True),
        ),
    ]
