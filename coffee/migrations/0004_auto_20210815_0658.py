# Generated by Django 3.2 on 2021-08-15 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_alter_dim_coffee_roaster_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dim_coffee',
            name='country_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='coffees', to='coffee.countries'),
        ),
        migrations.AlterField(
            model_name='dim_coffee',
            name='varietals',
            field=models.ManyToManyField(related_name='varieties', to='coffee.dim_varietal'),
        ),
    ]
