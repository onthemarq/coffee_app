# Generated by Django 3.2 on 2021-08-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0016_auto_20210820_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_coffee',
            name='elevation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dim_coffee',
            name='farmer',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
