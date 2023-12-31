# Generated by Django 3.2.22 on 2023-10-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20231014_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='platform',
            field=models.CharField(choices=[('Dreamcast', 'Dreamcast'), ('Gameboy', 'Gameboy'), ('Gameboy Color', 'Gameboy Color'), ('NES', 'NES'), ('N64', 'N64'), ('PC', 'PC'), ('PlayStation', 'PlayStation'), ('PlayStation 2', 'PlayStation 2'), ('Sega Genesis', 'Sega Genesis'), ('SNES', 'SNES'), ('XBOX', 'XBOX')], default='', max_length=100),
        ),
    ]
