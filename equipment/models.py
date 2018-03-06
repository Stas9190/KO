from django.db import models
from django.urls import reverse
from django.utils import timezone

# Узел оборудования
class Unit(models.Model):
    name = models.CharField('Наименование', max_length=200, null=False)
    description = models.CharField('Описание работ', max_length=200, null=False)
    time = models.IntegerField('Время выполнения', null=False)
    periodicity = models.IntegerField('Периодичность', null=False)
    date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name

# Тип оборудования
class equipmentType(models.Model):
    name = models.CharField('Наименование', max_length=200, null=False)
    model = models.CharField('Модель', max_length=200)
    inv_number = models.CharField('Инвентарный номер', max_length=200, null=False)
    date = models.DateTimeField(blank=True, null=True)
    #! Связь многие ко многим, equipment <--> unit
    equipment = models.ManyToManyField(Unit, verbose_name = 'Выбрать узлы')

    def get_absolute_url(self):
        return reverse('home')
    
    def __str__(self):
        return self.name


