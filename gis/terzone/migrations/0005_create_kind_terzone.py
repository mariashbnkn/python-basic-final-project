# Generated by Django 4.2.2 on 2023-08-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terzone', '0004_change_srid_terzone'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindTerzone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
