# Generated by Django 4.2.2 on 2023-08-23 19:18

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TerzoneExist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=100)),
                ('kind_obj', models.IntegerField(max_length=8)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('geom_type', models.CharField(max_length=20)),
                ('status', models.IntegerField(choices=[(0, 'Archived'), (1, 'Available')])),
            ],
        ),
    ]
