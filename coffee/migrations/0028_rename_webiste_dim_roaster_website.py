# Generated by Django 3.2 on 2021-09-10 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0027_auto_20210910_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dim_roaster',
            old_name='webiste',
            new_name='website',
        ),
    ]