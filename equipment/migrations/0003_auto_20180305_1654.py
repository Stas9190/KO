# Generated by Django 2.0.2 on 2018-03-05 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_auto_20180305_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('description', models.CharField(max_length=200, verbose_name='Описание работ')),
                ('time', models.IntegerField(verbose_name='Время выполнения')),
                ('peridicity', models.IntegerField(verbose_name='Периодичность')),
            ],
        ),
        migrations.AlterField(
            model_name='equipmenttype',
            name='inv_number',
            field=models.CharField(max_length=200, verbose_name='Инвентарный номер'),
        ),
        migrations.AddField(
            model_name='unit',
            name='equipment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipmentType'),
        ),
    ]
