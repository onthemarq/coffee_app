# Generated by Django 3.2 on 2021-08-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0014_alter_dim_coffee_roaster_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='name_long',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dim_coffee',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dim_notes',
            name='flavor_notes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dim_roaster',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
