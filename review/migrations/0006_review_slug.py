# Generated by Django 3.2.22 on 2023-10-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0005_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(default='review', max_length=200, unique=True),
        ),
    ]
