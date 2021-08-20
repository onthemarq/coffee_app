# Generated by Django 3.2 on 2021-08-17 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0007_auto_20210817_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='acidity',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='complexity',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='sweetness',
        ),
        migrations.AlterField(
            model_name='ratings',
            name='coffee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='rate', to='coffee.dim_coffee'),
        ),
    ]
