# Generated by Django 3.0 on 2022-08-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0027_auto_20220724_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fungi',
            options={'managed': True, 'verbose_name': 'Fungi', 'verbose_name_plural': 'Fungi'},
        ),
        migrations.AlterModelOptions(
            name='netlinks',
            options={'managed': True, 'ordering': ['OrderToDisplay'], 'verbose_name': 'NetLinks', 'verbose_name_plural': 'NetLinks'},
        ),
        migrations.AddField(
            model_name='habitat',
            name='Environment',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='latinsynonyms',
            name='LatinSynonym',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True, verbose_name='Synonym'),
        ),
        migrations.AlterField(
            model_name='latinsynonyms',
            name='LatinSynonymSource',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='status',
            name='RecordedInUK',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='NoData', max_length=255, null=True),
        ),
    ]
