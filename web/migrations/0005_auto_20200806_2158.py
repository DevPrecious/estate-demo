# Generated by Django 3.0.5 on 2020-08-06 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_house_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='Bathub_Amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='house',
            name='Bed_Amount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='house',
            name='Floor_plan_or_Height',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='house',
            name='url',
            field=models.SlugField(blank='Do not touch this', max_length=500, unique=True),
        ),
    ]
