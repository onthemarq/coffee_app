# Generated by Django 3.2 on 2021-09-11 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0030_alter_dim_coffee_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_coffee',
            name='process',
            field=models.CharField(choices=[('Washed', 'Washed'), ('Natural', 'Natural'), ('Anaerobic Natural', 'Anaerobic Natural'), ('Pulp Natural', 'Pulp Natural'), ('Honey', 'Honey'), ('Yellow Honey', 'Yellow Honey'), ('Honey Washed', 'Honey Washed'), ('Honey Natural', 'Honey Natural'), ('EA Decaf', 'EA Decaf'), ('Swiss Water Decaf', 'Swiss Water Decaf'), ('Mixed Process', 'Mixed Process'), ('Wet-hulled', 'Wet-hulled'), ('Experimental', 'Experimental')], max_length=100, null=True),
        ),
    ]