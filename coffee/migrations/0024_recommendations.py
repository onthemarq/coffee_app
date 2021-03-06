# Generated by Django 3.2 on 2021-09-03 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee', '0023_alter_ratings_brew_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='recommendations',
            fields=[
                ('rec_id', models.AutoField(primary_key=True, serialize=False)),
                ('rec_num', models.IntegerField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('coffee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recs', related_query_name='recs', to='coffee.dim_coffee')),
                ('user_id', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
