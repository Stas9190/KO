# Generated by Django 2.0.2 on 2018-03-05 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0006_unit_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='peridicity',
            new_name='periodicity',
        ),
    ]
