# Generated by Django 2.0.2 on 2018-03-16 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_equip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_quantity', models.DecimalField(decimal_places=0, max_digits=18)),
            ],
        ),
        migrations.AlterField(
            model_name='equip',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='maintenance',
            name='equip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='equipment.Equip'),
        ),
    ]