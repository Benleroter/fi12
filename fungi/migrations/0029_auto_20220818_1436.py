# Generated by Django 3.0 on 2022-08-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0028_auto_20220816_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fruitingbody',
            name='ColourDescription',
        ),
        migrations.AlterField(
            model_name='fruitingbody',
            name='Colour',
            field=models.CharField(blank=True, default='NoData', max_length=1028, null=True),
        ),
    ]