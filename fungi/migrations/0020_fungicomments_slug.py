# Generated by Django 3.0 on 2021-12-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fungi', '0019_fungi_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='fungicomments',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
