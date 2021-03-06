# Generated by Django 2.0.2 on 2018-03-15 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('inv_number', models.CharField(max_length=100)),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='equipment.Equipment')),
                ('units', models.ManyToManyField(to='equipment.Unit')),
            ],
        ),
    ]
