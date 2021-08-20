# Generated by Django 3.2 on 2021-08-18 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0011_alter_dim_coffee_process'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_coffee',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coffees', to='coffee.countries'),
        ),
        migrations.AlterField(
            model_name='dim_coffee',
            name='roaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coffees', to='coffee.dim_roaster'),
        ),
    ]