# Generated by Django 3.0 on 2021-11-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0009_auto_20211023_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latinsynonyms',
            name='LatinSynonym',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='othercommonnames',
            name='AltCommonName',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='similarfungi',
            name='SimilarFungiName',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True, verbose_name=''),
        ),
    ]
