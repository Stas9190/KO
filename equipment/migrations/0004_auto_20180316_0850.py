# Generated by Django 2.0.2 on 2018-03-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_auto_20180316_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='equip',
            field=models.DecimalField(decimal_places=0, max_digits=18),
        ),
    ]
