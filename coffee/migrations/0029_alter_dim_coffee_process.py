# Generated by Django 3.2 on 2021-09-10 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0028_rename_webiste_dim_roaster_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_coffee',
            name='process',
            field=models.CharField(choices=[('Washed', 'Washed'), ('Natural', 'Natural'), ('Anaerobic Natural', 'Anaerobic Natural'), ('Pulp Natural', 'Pulp Natural'), ('Honey', 'Honey'), ('Yellow Honey', 'Yellow Honey'), ('Honey Washed', 'Honey Washed'), ('Honey Natural', 'Honey Natural'), ('EA Decaf', 'EA Decaf'), ('Swiss Water Decaf', 'Swiss Water Decaf'), ('Mixed Process', 'Mixed Process'), ('Wet-hulled', 'Wet-hulled'), ('Experimental', 'Experimental')], max_length=20, null=True),
        ),
    ]