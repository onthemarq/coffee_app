# Generated by Django 3.2 on 2021-08-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0019_alter_ratings_coffee'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratings',
            name='rating_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
