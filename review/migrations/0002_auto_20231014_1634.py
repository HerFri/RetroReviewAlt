# Generated by Django 3.2.22 on 2023-10-14 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Arcade', 'Arcade'), ('Beat Em Up', 'Beat Em Up'), ('Ego-Shooter', 'Ego-Shooter'), ('Platformer', 'Platformer'), ('Racing', 'Racing'), ('RPG', 'RPG'), ('Simulation', 'Simulation'), ('Sports', 'Sports'), ('Strategy', 'Strategy'), ('Puzzle', 'Puzzle'), ('Horror', 'Horror')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='year',
            field=models.IntegerField(choices=[(1980, '1980'), (1981, '1981'), (1982, '1982'), (1983, '1983'), (1984, '1984'), (1985, '1985'), (1986, '1986'), (1987, '1987'), (1988, '1988'), (1989, '1989'), (1990, '1990'), (1991, '1991'), (1992, '1992'), (1993, '1993'), (1994, '1994'), (1995, '1995'), (1996, '1996'), (1997, '1997'), (1998, '1998'), (1999, '1999'), (2000, '2000'), (2001, '2001'), (2002, '2002'), (2003, '2003'), (2004, '2004'), (2005, '2005'), (2006, '2006'), (2007, '2007'), (2008, '2008')], default=1980),
        ),
    ]
