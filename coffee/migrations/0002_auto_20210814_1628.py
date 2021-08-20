# Generated by Django 3.2 on 2021-08-14 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('country_code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('country_code_alpha', models.CharField(max_length=2, null=True)),
                ('country_code_alpha3', models.CharField(max_length=3, null=True)),
                ('name_long', models.CharField(max_length=50, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dim_coffee',
            name='country_code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coffee.countries'),
        ),
        migrations.DeleteModel(
            name='dim_country',
        ),
    ]
