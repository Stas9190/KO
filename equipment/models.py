from django.db import models
from django.urls import reverse
from django.utils import timezone

# Тип оборудования
class equipmentType(models.Model):
    name = models.CharField('Наименование', max_length=200, null=False)
    model = models.CharField('Модель', max_length=200)
    date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('home')

    # Создать новую единицу оборудования
    #def create(self):
    #    self.date = timezone.now()
    #    self.save()
    
    def __str__(self):
        return self.name

