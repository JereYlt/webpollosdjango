# Generated by Django 3.0.8 on 2022-09-16 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]
