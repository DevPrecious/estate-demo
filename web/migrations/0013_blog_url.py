# Generated by Django 3.0.5 on 2020-08-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.SlugField(blank='Do not touch this', max_length=500, unique=True),
        ),
    ]