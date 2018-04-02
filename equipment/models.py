from django.db import models
from django.urls import reverse
from django.utils import timezone
from smart_selects.db_fields import ChainedManyToManyField

# Узлы оборудования
class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    id_unitgroup = models.ForeignKey('Untigroup', models.DO_NOTHING, db_column='id_unitGroup', verbose_name='Выбор группы')  # Field name made lowercase.
    name = models.CharField('Наименование', max_length=200)
    description = models.CharField('Описание работ', max_length=500)
    executor = models.CharField('Исполнитель работ', max_length=200)
    time = models.DecimalField('Время выполнения (мин.)', max_digits=18, decimal_places=0)
    periodicity = models.DecimalField('Периодичность (дн.)', max_digits=18, decimal_places=0, blank=True, null=True)
    photo = models.FileField(upload_to='media/', max_length=50, blank=True, null=True, verbose_name='Изображение')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Unit'
    
    def __str__(self):
        return self.name

# Типы оборудования
class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Наименование', max_length=50, blank=True, null=True)
    model = models.CharField('Модель', max_length=200)
    #inv_number = models.CharField('Инвентарный номер', max_length=100)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Equipment'
    
    def get_absolute_url(self):
        return reverse('equipment_list')
    
    def __str__(self):
        return self.name

# Группы узлов оборудования
class Untigroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'untiGroup'
    
    def __str__(self):
        return self.name

# Создаем новое оборудование и определяем связь с узлами
class Equip(models.Model):
    inv_number = models.CharField(max_length=100)
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    units = models.ManyToManyField(
        Unit,
        through='EquipmentEquipUnits',
        through_fields=('equip', 'unit'),
    )

# Обслуживание
class Maintenance(models.Model):
    id_equip = models.DecimalField(max_digits=18, decimal_places=0)
    actual_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenance'

# Связка между Equip и Unit
class EquipmentEquipUnits(models.Model):
    equip = models.ForeignKey(Equip, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    fact = models.IntegerField(default=0) # Фактическое время наработки

    class Meta:
        managed = False
        db_table = 'equipment_equip_units'
        unique_together = (('equip', 'unit'),)
        auto_created = True    #!!!! при использовании through добавить это

# Выполненные работы
class Work(models.Model):
    id_user = models.IntegerField()
    id_maintaince = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'work'

#Соответствия между узлами и типами оборудования
#class Junction(models.Model):
 #   id = models.AutoField(primary_key=True)
  #  id_unit = models.DecimalField(max_digits=18, decimal_places=0)
   # id_equipment = models.DecimalField(max_digits=18, decimal_places=0)

    #class Meta:
     #   managed = False
      #  db_table = 'Junction'