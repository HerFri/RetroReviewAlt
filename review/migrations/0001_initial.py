# Generated by Django 3.2.22 on 2023-10-13 21:45

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('description', models.TextField()),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('excerpt', models.TextField(blank=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('rating', models.DecimalField(choices=[(0, '0.0 Stars'), (0.5, '0.5 Stars'), (1, '1.0 Stars'), (1.5, '1.5 Stars'), (2, '2.0 Stars'), (2.5, '2.5 Stars'), (3, '3.0 Stars'), (3.5, '3.5 Stars'), (4, '4.0 Stars'), (4.5, '4.5 Stars'), (5, '5.0 Stars')], decimal_places=1, max_digits=2)),
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.game')),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
