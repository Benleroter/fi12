# Generated by Django 3.0 on 2021-10-12 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0004_remove_similarfungi_similarfungiid'),
    ]

    operations = [
        migrations.AddField(
            model_name='similarfungi',
            name='SimilarFungiId',
            field=models.CharField(blank=True, default='NoData', max_length=255, null=True),
        ),
    ]
