# Generated by Django 3.2.9 on 2022-05-28 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0013_alter_wmoprogram_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationvariable',
            name='test_persistence_interval',
        ),
        migrations.RemoveField(
            model_name='stationvariable',
            name='test_persistence_variance',
        ),
        migrations.RemoveField(
            model_name='stationvariable',
            name='test_spike_value',
        ),
    ]